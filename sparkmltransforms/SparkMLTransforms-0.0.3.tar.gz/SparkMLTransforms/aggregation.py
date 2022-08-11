from typing import Dict, List, Optional

import pandas as pd
import pyspark.sql.functions as F
from pyspark.sql import DataFrame
from pyspark.sql.types import StringType

from SparkMLTransforms.base import IdentityFitTransformer


@F.udf(returnType=StringType())
def get_mode_udf(list_of_things):
    if len(list_of_things) == 0:
        return None
    mode_values = pd.Series(list_of_things).mode()
    if len(mode_values) == 0:
        return None
    else:
        return mode_values.iloc[0]


class AggregatedFeatures(IdentityFitTransformer):
    def __init__(self, input_columns: List[str], group_columns: List[str], categorical_columns: Optional[List[str]] = None) -> None:
        self.input_columns = input_columns
        self.group_columns = group_columns
        self.categorical_columns = [] if categorical_columns is None else categorical_columns

    def input_output_columns(self) -> Dict[str, List[str]]:
        d = {None: 'num_rows'}
        for c in self.input_columns:
            if c in self.categorical_columns:
                d[c] = [f'{c}_num_unique', f'{c}_mode']
            else:
                d[c] = [f'{c}_min', f'{c}_max', f'{c}_mean']
        return d

    def transform(self, df: DataFrame) -> DataFrame:
        agg_cols = [F.count('*').alias('num_rows')]
        for c in self.input_columns:
            if c in self.categorical_columns:
                agg_cols += [
                    F.size(F.collect_set(c)).alias(f'{c}_num_unique'),
                    get_mode_udf(F.collect_list(c)).alias(f'{c}_mode'),
                ]
            else:
                agg_cols += [
                    F.size(F.collect_set(c)).alias(f'{c}_num_unique'),
                    F.min(c).alias(f'{c}_min'),
                    F.max(c).alias(f'{c}_max'),
                    F.mean(c).alias(f'{c}_mean'),
                ]
        return (
            df
            .groupBy(self.group_columns)
            .agg(*agg_cols)
        )
