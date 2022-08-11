import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from pyspark.sql import SparkSession

from SparkMLTransforms.lagged import LaggedFeatures


@pytest.mark.parametrize(
    ('input_df', 'expected_df'),
    [
        pytest.param(
            pd.DataFrame({
                'a': [1, 2, 3],
                'g': ['1', '1', '2'],
                'o': [1, 2, 3],
            }),
            pd.DataFrame({
                'g': ['1', '2'],
                'a_lag_0': [2, 3],
                'a_lag_1': [1, None],
            }),
            id='simple'
        ),
    ]
)
def test_LaggedFeatures(spark: SparkSession, input_df: pd.DataFrame, expected_df: pd.DataFrame):
    input_df = spark.createDataFrame(input_df)
    output_df = LaggedFeatures(
        input_columns=['a'],
        group_columns=['g'],
        order_column='o',
        lags=[0, 1],
        filter_latest=True,
    ).fit_transform(input_df)
    output_df = output_df.toPandas()
    assert_frame_equal(output_df, expected_df)
