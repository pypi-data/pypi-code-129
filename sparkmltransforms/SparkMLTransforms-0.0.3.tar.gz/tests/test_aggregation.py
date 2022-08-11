import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from pyspark.sql import SparkSession

from SparkMLTransforms.aggregation import AggregatedFeatures


@pytest.mark.parametrize(
    ('input_df', 'expected_df'),
    [
        pytest.param(
            pd.DataFrame({
                'a': [1, 2, 3],
                'b': ['a', 'a', 'b'],
                'g': ['1', '1', '2'],
            }),
            pd.DataFrame({
                'g': ['1', '2'],
                'num_rows': [2, 1],
                'a_num_unique': [2, 1],
                'a_min': [1, 3],
                'a_max': [2, 3],
                'a_mean': [1.5, 3],
                'b_num_unique': [1, 1],
                'b_mode': ['a', 'b'],
            }),
            id='simple'
        ),
    ]
)
def test_AggregatedFeatures(spark: SparkSession, input_df: pd.DataFrame, expected_df: pd.DataFrame):
    input_df = spark.createDataFrame(input_df)
    output_df = AggregatedFeatures(
        input_columns=['a', 'b'],
        group_columns=['g'],
        categorical_columns=['b'],
    ).fit_transform(input_df)
    output_df = output_df.toPandas()
    assert_frame_equal(output_df, expected_df, check_dtype=False)
