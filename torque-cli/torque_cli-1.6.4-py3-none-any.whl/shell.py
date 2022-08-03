"""
Usage: torque [--space=<space>] [--token=<token>] [--account=<account>] [--profile=<profile>] [--help] [--debug]
               [--disable-version-check] <command> [<args>...]

Options:
  -h --help                 Show this screen.

  --version                 Show current version

  --space=<space>           Use a specific Torque Space, this will override any default set in the config file

  --token=<token>           Use a specific token for authentication, this will override any default set in the
                            config file

  --account=<account>       [Optional] Your Torque account name. The account name is equal to your subdomain in
                            the Torque URL. e.g. https://YOURACCOUNT.qtorque.io/

  --profile=<profile>       Use a specific Profile section in the config file
                            You still can override config with --token/--space options.

  --disable-version-check   Do not check whether a new version of torque is available for download.

Commands:
    bp, blueprint       validate torque blueprints
    sb, sandbox         start sandbox, end sandbox and get its status
    configure           set, list and remove connection profiles to torque
"""
import logging
import sys

import pkg_resources
from colorama import init
from docopt import DocoptExit, docopt

from torque.commands import bp, configure, sb
from torque.models.connection import TorqueConnection
from torque.parsers.global_input_parser import GlobalInputParser
from torque.services.connection import TorqueConnectionProvider
from torque.services.version import VersionCheckService

logger = logging.getLogger(__name__)

commands_table = {
    "bp": bp.BlueprintsCommand,
    "blueprint": bp.BlueprintsCommand,
    "sb": sb.SandboxesCommand,
    "sandbox": sb.SandboxesCommand,
    "configure": configure.ConfigureCommand,
}


class BootstrapHelper:
    @staticmethod
    def is_help_message_requested(input_parser: GlobalInputParser) -> bool:
        if not input_parser.command_args:
            return True

        return "--help" in input_parser.command_args or "-h" in input_parser.command_args

    @staticmethod
    def get_connection_params(input_parser: GlobalInputParser) -> TorqueConnection:
        # Take auth parameters
        if BootstrapHelper.should_get_connection_params(input_parser):
            connection_provider = TorqueConnectionProvider(input_parser)
            conn = connection_provider.get_connection()
        else:
            # no need to init connection object, the command will show help message and exit or will start
            # interactive config
            conn = None

        return conn

    @staticmethod
    def validate_command(command_name: str) -> None:
        if command_name not in commands_table:
            raise DocoptExit("Invalid or unknown command. See usage instruction by running 'torque -h'")

    @staticmethod
    def is_config_mode(input_parser: GlobalInputParser) -> bool:
        return input_parser.command == "configure"

    @staticmethod
    def should_get_connection_params(input_parser: GlobalInputParser) -> bool:
        return not BootstrapHelper.is_help_message_requested(input_parser) and not BootstrapHelper.is_config_mode(
            input_parser
        )


def main():
    # Colorama init for colored output
    init()
    version = pkg_resources.get_distribution("torque-cli").version
    args = docopt(__doc__, options_first=True, version=version)
    input_parser = GlobalInputParser(args)

    # Check for new version
    if not input_parser.disable_version_check:
        VersionCheckService(version).check_for_new_version_safely()

    level = logging.DEBUG if input_parser.debug else logging.WARNING
    logging.basicConfig(format="%(levelname)s - %(message)s", level=level)

    # Validate command
    BootstrapHelper.validate_command(input_parser.command)

    # Take auth parameters
    conn = BootstrapHelper.get_connection_params(input_parser)

    argv = [input_parser.command] + input_parser.command_args

    command_class = commands_table[input_parser.command]
    command = command_class(argv, conn)
    result = command.execute()

    exit(result)


def exit(run_result) -> None:
    if not run_result:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
