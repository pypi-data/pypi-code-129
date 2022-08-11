"""Parser module to parse gear config.json."""
import logging
from typing import Tuple

from flywheel_gear_toolkit import GearToolkitContext

from .oct_qa import OCTqa

log = logging.getLogger(__name__)


def parse_config(
    gear_context: GearToolkitContext,
) -> (OCTqa, bool):
    """This function mainly parses gear_context's config.json file and returns relevant inputs and options.
    Args:
        - gear_context: GearToolkitContext.
    Returns:
        ophtha_qa: OCTqa class instance.
        debug: bool
            Whether to set logging to debug.
    """
    # Get the path to the raw input file and other config params
    path_raw_input = gear_context.get_input_path("raw_input")
    debug = gear_context.config.get("debug")
    save_figures_if_fail = gear_context.config.get("save_figures_if_fail")

    # Use an interface for the different file types
    ophtha_qa = OCTqa.factory(
        path_file=path_raw_input,
        output_dir=gear_context.output_dir,
        work_dir=gear_context.work_dir,
        save_figures_if_fail=save_figures_if_fail,
    )

    return ophtha_qa, debug
