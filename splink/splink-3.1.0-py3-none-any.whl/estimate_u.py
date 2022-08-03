import logging
from copy import deepcopy
from typing import TYPE_CHECKING

from .blocking import block_using_rules_sql
from .comparison_vector_values import compute_comparison_vector_values_sql
from .expectation_maximisation import (
    compute_new_parameters_sql,
    compute_proportions_for_new_parameters,
)

from .m_u_records_to_parameters import (
    m_u_records_to_lookup_dict,
    append_u_probability_to_comparison_level_trained_probabilities,
)

# https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports
if TYPE_CHECKING:
    from .linker import Linker

logger = logging.getLogger(__name__)


def _num_target_rows_to_rows_to_sample(target_rows):
    # Number of rows generated by cartesian product is
    # n(n-1)/2, where n is input rows
    # We want to set a target_rows = t, the number of
    # rows generated by Splink and find out how many input rows
    # we need to generate target rows
    #     Solve t = n(n-1)/2 for n
    #     https://www.wolframalpha.com/input/?i=Solve%5Bt%3Dn+*+%28n+-+1%29+%2F+2%2C+n%5D
    sample_rows = 0.5 * ((8 * target_rows + 1) ** 0.5 + 1)
    return sample_rows


def estimate_u_values(linker: "Linker", target_rows):

    logger.info("----- Estimating u probabilities using random sampling -----")

    original_settings_obj = linker._settings_obj

    training_linker = deepcopy(linker)

    training_linker._train_u_using_random_sample_mode = True

    settings_obj = training_linker._settings_obj
    settings_obj._retain_matching_columns = False
    settings_obj._retain_intermediate_calculation_columns = False
    settings_obj._training_mode = True
    for cc in settings_obj.comparisons:
        for cl in cc.comparison_levels:
            cl._level_dict["tf_adjustment_column"] = None

    sql = """
    select count(*) as count
    from __splink__df_concat_with_tf
    """
    dataframe = training_linker._sql_to_splink_dataframe_checking_cache(
        sql, "__splink__df_concat_count"
    )
    result = dataframe.as_record_dict()
    dataframe.drop_table_from_database()
    count_rows = result[0]["count"]

    if settings_obj._link_type in ["dedupe_only", "link_and_dedupe"]:
        sample_size = _num_target_rows_to_rows_to_sample(target_rows)
        proportion = sample_size / count_rows

    if settings_obj._link_type == "link_only":
        sample_size = target_rows**0.5
        proportion = sample_size / count_rows

    if proportion >= 1.0:
        proportion = 1.0

    if sample_size > count_rows:
        sample_size = count_rows

    sql = f"""
    select *
    from __splink__df_concat_with_tf
    {training_linker._random_sample_sql(proportion, sample_size)}
    """

    df_sample = training_linker._sql_to_splink_dataframe_checking_cache(
        sql,
        "__splink__df_concat_with_tf_sample",
        transpile=False,
    )

    settings_obj._blocking_rules_to_generate_predictions = []

    sql = block_using_rules_sql(training_linker)
    training_linker._enqueue_sql(sql, "__splink__df_blocked")

    # repartition after blocking only exists on the SparkLinker
    repartition_after_blocking = getattr(
        training_linker, "repartition_after_blocking", False
    )
    if repartition_after_blocking:
        df_blocked = training_linker._execute_sql_pipeline([df_sample])
        input_dataframes = [df_blocked]
    else:
        input_dataframes = [df_sample]

    sql = compute_comparison_vector_values_sql(settings_obj)

    training_linker._enqueue_sql(sql, "__splink__df_comparison_vectors")

    sql = """
    select *, cast(0.0 as double) as match_probability
    from __splink__df_comparison_vectors
    """

    training_linker._enqueue_sql(sql, "__splink__df_predict")

    sql = compute_new_parameters_sql(settings_obj)
    linker._enqueue_sql(sql, "__splink__m_u_counts")
    df_params = training_linker._execute_sql_pipeline(input_dataframes)

    param_records = df_params.as_pandas_dataframe()
    param_records = compute_proportions_for_new_parameters(param_records)
    df_params.drop_table_from_database()
    df_sample.drop_table_from_database()

    m_u_records = [
        r
        for r in param_records
        if r["output_column_name"] != "_probability_two_random_records_match"
    ]

    m_u_records_lookup = m_u_records_to_lookup_dict(m_u_records)
    for c in original_settings_obj.comparisons:
        for cl in c._comparison_levels_excluding_null:
            append_u_probability_to_comparison_level_trained_probabilities(
                cl, m_u_records_lookup, "estimate u by random sampling"
            )

    logger.info("\nEstimated u probabilities using random sampling")
