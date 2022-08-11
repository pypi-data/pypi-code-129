import logging

import numpy as np

log = logging.getLogger(__name__)


def format_qc_metadata(
    qa_index,
):
    """
    Formats the quality index metadata of the OCT slices.

    Params
    ------
    qa_index: dict
        Keys:
        - Slopes: array. Mean slope in transition between extra-retinal and intra-retinal regions of the OCT data.
        - Variance extraretinal: array. Mean variance of extra-retinal region of the OCT data.
        - Variance intraretinal: array. Mean variance of intra-retinal region of the OCT data.
        - Dynamic range: array. Mean Dynamic Range (ratio of brightest and darkest pixels) of OCT data
        - Outliers Slope: slice index of slices that have a slope above or below 1.5 times the Interquartile Range
        - Outliers Variance Extraretinal: slice index of slices that have a extraretinal variance above or below 1.5 times the Interquartile Range
        - Outliers Variance Intraretinal: slice index of slices that have a intraaretinal variance above or below 1.5 times the Interquartile Range
        - Outliers Dynamic range: slice index of slices that have a dynamic range above or below 1.5 times the Interquartile Range

    Returns
    -------
    qc_names: list
        A list of strings, each one as the name of the qc test.
    qc_tests: list
        A list of strings, can only be 'pass' or 'fail'.
    qc_data: list
        A list of dicts, each one with at least one key:value pair. Data
        supporting qc test results.
    """

    # Map each qa measurement/index to either 'pass' or 'fail'. If no slices
    # have been flagged for a test, it passes.
    if not qa_index["Outliers Dynamic range"]:
        qa_index["Outliers Dynamic range"] = "No slices flagged"
        dr_test = "pass"
    else:
        dr_test = "fail"
    if not qa_index["Outliers Variance Extraretinal"]:
        qa_index["Outliers Variance Extraretinal"] = "No slices flagged"
        var_ext_test = "pass"
    else:
        var_ext_test = "fail"
    if not qa_index["Outliers Variance Intraretinal"]:
        qa_index["Outliers Variance Intraretinal"] = "No slices flagged"
        var_int_test = "pass"
    else:
        var_int_test = "fail"
    if not qa_index["Outliers Sharpness slope"]:
        qa_index["Outliers Sharpness slope"] = "No slices flagged"
        sharp_slope_test = "pass"
    else:
        sharp_slope_test = "fail"

    # create data for each test
    dr_data = {
        "Mean Dynamic range": round(np.mean(qa_index["Dynamic range"]), 3),
        "Standard deviation Dynamic range": round(np.std(qa_index["Dynamic range"]), 3),
        "Outliers Dynamic range": qa_index["Outliers Dynamic range"],
    }
    var_ext_data = {
        "Mean Variance Extraretinal region": round(
            np.mean(qa_index["Variance extraretinal"]), 3
        ),
        "Standard deviation Variance Extraretinal region": round(
            np.std(qa_index["Variance extraretinal"]), 3
        ),
        "Outliers Variance Extraretinal": qa_index["Outliers Variance Extraretinal"],
    }
    var_int_data = {
        "Mean Variance Intraretinal": round(
            np.mean(qa_index["Variance intraretinal"]), 3
        ),
        "Standard deviation Variance Intraretinal": round(
            np.std(qa_index["Variance intraretinal"]), 3
        ),
        "Outliers Variance Intraretinal": qa_index["Outliers Variance Intraretinal"],
    }
    sharp_slope_data = {
        "Mean Sharpness slope": round(np.mean(qa_index["Sharpness slope"]), 3),
        "Standard deviation Sharpness slope": round(
            np.std(qa_index["Sharpness slope"]), 3
        ),
        "Outliers Sharpness slope": qa_index["Outliers Sharpness slope"],
    }

    # Set overall qc/qa test
    qc_tests = [dr_test, var_ext_test, var_int_test, sharp_slope_test]
    qc_names = [
        "dynamic_range",
        "variance_extraretinal",
        "variance_intraretinal",
        "sharpness_slope",
    ]
    if "fail" in qc_tests:
        overall_qc_test = "fail"
        qc_tests_failed_str = ", ".join(
            [name for test, name in zip(qc_tests, qc_names) if test == "fail"]
        )
        overall_qc_data = {"result": "'%s' qc test(s) failed." % qc_tests_failed_str}
        log.warning("'%s' qc test(s) failed." % qc_tests_failed_str)
    else:
        overall_qc_test = "pass"
        overall_qc_data = {"result": "all qc tests passed"}

    qc_tests.append(overall_qc_test), qc_names.append("overall_qc")
    qc_data = [dr_data, var_ext_data, var_int_data, sharp_slope_data, overall_qc_data]

    # store qc results
    log.debug("qc_names: %s" % qc_names)
    log.debug("qc_tests: %s" % qc_tests)
    log.debug("qc_data: %s" % qc_data)

    return qc_names, qc_tests, qc_data


def update_qc_metadata(my_gear_context, input_name: str, qc_names, qc_tests, qc_data):
    """
    Updates a file's info dictionary with oct qa/qc results.

    Each element of qc_names, qc_tests, and qc_data should correspond with each
    other.

    Params
    ------
    gear_context: GearToolkitContext object.
    input_name: str
        The name of the input file to update.
    qc_names: list
        A list of strings, each one as the name of the qc test.
    qc_tests: list
        A list of strings, can only be 'pass' or 'fail'.
    qc_data: list
        A list of dicts, each one with at least one key:value pair. Data
        supporting qc test results.

    Returns
    -------
    None
    """
    raw_input = my_gear_context.get_input_filename(input_name)

    for qc_name, qc_test, qc_datum in zip(qc_names, qc_tests, qc_data):
        my_gear_context.metadata.add_qc_result(
            file_=raw_input, name=qc_name, state=qc_test, data=qc_datum
        )
