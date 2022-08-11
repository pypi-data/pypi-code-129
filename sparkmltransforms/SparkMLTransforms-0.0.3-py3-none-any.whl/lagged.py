from typing import Dict, List

import pyspark.sql.functions as F
from pyspark.sql import DataFrame
from pyspark.sql.window import Window

from SparkMLTransforms.base import IdentityFitTransformer

__LATEST_ORDER_COLUMN_VALUE__ = '__LATEST_ORDER_COLUMN_VALUE__'


class LaggedFeatures(IdentityFitTransformer):
    def __init__(
        self,
        input_columns: List[str],
        group_columns: List[str],
        order_column: str,
        lags: List[int] = [0, 1],
        filter_latest: bool = True,
    ) -> None:
        self.input_columns = input_columns
        self.group_columns = group_columns
        self.order_column = order_column
        self.lags = lags
        self.filter_latest = filter_latest

    def get_latest(self, df: DataFrame) -> DataFrame:
        return (
            df
            .groupBy(*self.group_columns)
            .agg(F.max(self.order_column).alias(__LATEST_ORDER_COLUMN_VALUE__))
            .cache()
        )

    def input_output_columns(self) -> Dict[str, List[str]]:
        d = {}
        for c in self.input_columns:
            d[c] = [f'{c}_lag_{i}' for i in self.lags]
        return d

    def transform(self, df: DataFrame) -> DataFrame:
        df_latest = self.get_latest(df=df)
        window = (
            Window
            .partitionBy(self.group_columns)
            .orderBy(self.order_column)
        )
        select_cols = self.group_columns.copy()
        if self.filter_latest:
            select_cols.append(F.col(self.order_column).alias(__LATEST_ORDER_COLUMN_VALUE__))
        for c in self.input_columns:
            select_cols += [
                F.lag(c, offset=i).over(window).alias(f'{c}_lag_{i}')
                for i in self.lags
            ]
        df = df.select(*select_cols)
        if self.filter_latest:
            join_cols = [*self.group_columns, __LATEST_ORDER_COLUMN_VALUE__]
            df = (
                df
                .join(df_latest, on=join_cols, how='inner')
                .drop(__LATEST_ORDER_COLUMN_VALUE__)
            )
        return df
