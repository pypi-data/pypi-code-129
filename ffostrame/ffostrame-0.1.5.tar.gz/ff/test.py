import logging
from tkinter import W
import tabulate
import pprint
import rich_click as click


@click.group(help="Test something")
@click.pass_obj
@click.pass_context
def test(ctx, profile):

    profiles_dict = ctx
    ctx.obj = profiles_dict.obj
    pass


@test.command(help="Test subprocess")
@click.option("--log-level", required=True, default="info", help="Logging level")
@click.pass_obj
def subprocess(ctx, log_level):

    # do something with context if needed in near future
    # print(ctx)
    logging.basicConfig(level=log_level.upper())

    import subprocess

    from utils import Utils

    utils = Utils()

    ls_command_result = (subprocess.run(["ls", "-l", "/dev/null"], capture_output=True))
    if ls_command_result.returncode != 0:
        print(ls_command_result.stderr)
        utils.exit_error("Unable to run ls command")
    else:
        print('😁 Successful ran ls command')
        print('😁 Here is the stdout:')
        print(ls_command_result.stdout)
    try:
        sleep_result = subprocess.run(["sleep", "3"], timeout=1)
        print(sleep_result.returncode)
    except subprocess.TimeoutException as err:
        print(err)
