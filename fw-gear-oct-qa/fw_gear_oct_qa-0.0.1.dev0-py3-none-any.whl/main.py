"""Main module."""

import logging
import sys

from flywheel_gear_toolkit import GearToolkitContext

from fw_gear_oct_qa.format_qc import format_qc_metadata

from .oct_qa import OCTqa

log = logging.getLogger(__name__)


def run(ophtha_qa: OCTqa):
    """
    Calculates three indexes of OCT quality assessment.
    OCT Quality Assessment. Three indexes are calculated:
        1) mean and variance of the black region of the retinal image
        2) the slope of the image intensity measuring from the black region into the retina
        3) dynamic range of the retinal image.

    Args:
    ---------
    ophtha_qa: OCT-qa
        A concrete instance of OCT-qa.

    Returns
    -------
    qa_index: dict.
        Keys:
        - Sharpness slope: array. Mean slope in transition between extra-retinal and intra-retinal regions of the OCT data.
        - Variance extraretinal: array. Mean variance of extra-retinal region of the OCT data.
        - Variance intraretinal: array. Mean variance of intra-retinal region of the OCT data.
        - Dynamic range: array. Mean Dynamic Range (ratio of brightest and darkest pixels) of OCT data
        - Outliers Slope: slice index of slices that have a slope above or below 1.5 times the Interquartile Range
        - Outliers Variance Extraretinal: slice index of slices that have a extraretinal variance above or below 1.5 times the Interquartile Range
        - Outliers Variance Intraretinal: slice index of slices that have a intraaretinal variance above or below 1.5 times the Interquartile Range
        - Outliers Dynamic range: slice index of slices that have a dynamic range above or below 1.5 times the Interquartile Range
    qc_names: list
        A list of strings, each one as the name of the qc test.
    qc_tests: list
        A list of strings, can only be 'pass' or 'fail'.
    qc_data: list
        A list of dicts, each one with at least one key:value pair. Data
        supporting qc test results.
    """
    log.info("Starting OCT-qa gear...")
    log.info("Output directory: %s", ophtha_qa.output_dir)
    try:
        # Call the template method for aligning OCT slices
        qa_index, output_csv = ophtha_qa.assess_quality()

        qc_names, qc_tests, qc_data = format_qc_metadata(qa_index)

        # Save figures if config option 'save_figures_if_fail` is True
        if ophtha_qa.save_figures_if_fail:
            if "fail" in qc_tests:
                log.info("Generating QA histograms...")
                ophtha_qa.savefigures(output_csv)
                log.info("Saved figures")

    except Exception:
        log.exception("OCT quality assessment failed")
        log.info("Exiting...")
        sys.exit(1)
    else:
        log.info("Done with OCT-qa gear.")
        return 0, qa_index, qc_names, qc_tests, qc_data
