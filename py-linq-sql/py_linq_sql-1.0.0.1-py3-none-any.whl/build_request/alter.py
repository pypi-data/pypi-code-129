"""Build all alter commands."""

# Standard imports
from typing import Any, Dict, List, Set, Tuple

# Local imports
from ..exception.exception import DeleteError, NeedWhereError, TooManyReturnValueError
from ..utils.classes.magicdotpath import MagicDotPath
from ..utils.classes.other_classes import Command, SQLEnumerableData
from ..utils.functions.other_functions import get_json
from ..utils.functions.path_functions import get_path, get_update_path
from .consult import build_where


def build_delete(
    command: Command,
    sqle: SQLEnumerableData,
    built_commands: Set[int],
) -> str:
    """
    Build a delete request.

    Args:
        command: Command to build.
        sqle: SQLEnumerable with connection, flags, list of commands and a table.
        built_commands: All commands that have already been built.

    Returns:
        Request to execute.

    Raises:
        DeleteError: If len(sqle.cmd) > 1 and command.args.armagedon).
        NeedWhereError: If len(sqle.cmd) < 2.
        psycopg.Error: Indirect raise by `build_where`.
        TableError: Indirect raise by `build_where`.
        TypeError: Indirect raise by `build_where`.
        TypeOperatorError: Indirect raise by `build_where`.
    """
    armagedon = command.args.armagedon

    result = [f"DELETE FROM {sqle.table}"]

    if len(sqle.cmd) > 1 and armagedon:
        raise DeleteError("where")

    if armagedon:
        return result[0]

    if len(sqle.cmd) < 2:
        raise NeedWhereError()

    result.append(build_where(sqle, built_commands))

    # We use filter with None for the argument __function.
    # If we give None to the first element of filter
    # it will pass all the elements evaluate to false no matter why.
    #
    # We can have None in result if sqle.cmd contains commands
    # which will be evaluated later in build_where()
    return " ".join(filter(None, result))


def _build_json_insert(
    data: Dict[str, Any] | List[Dict[str, Any]],
    column: str,
    table: str,
) -> str:
    """
    Build an insert request for a json column.

    Args:
        data: Data to insert to the table.
        column: column of the data.
        table: Table where we want insert data.

    Returns:
        Request to execute.

    Raises:
        TypeError: If data is a list. In json insert we can't take multi columns.
        ValueError: Indirect raise by `get_json`.
    """
    if isinstance(column, list):
        raise TypeError("In json insert you can't give multi columns.")

    result = [f"INSERT INTO {table}({column}) VALUES"]

    match data:
        case dict():
            result.append(f"('{get_json(data)}')")
        case list():
            result.append(", ".join([f"('{get_json(d)}')" for d in data]))

    return " ".join(result)


def _build_relational_insert(
    data: Tuple | List[Tuple] | str,
    column: str | List[str],
    table: str,
) -> str:
    """
    Build an insert request for a relational column.

    Args:
        data: Data to insert to the table.
        column: column(s) of the data.
        table: Table where we want insert data.

    Returns:
        Request to execute.
    """
    result = [f"INSERT INTO {table}("]

    match column:
        case str():
            result.append(f"{column}")
            result.append(")")
        case _:
            result.append(", ".join(column))
            result.append(")")

    result.append("VALUES")

    match data:
        case tuple():
            result.append(str(data))
        case list():
            result.append(", ".join([str(d) for d in data]))
        case str():
            result.append(f"('{data}')")

    return " ".join(result)


def build_insert(command: Command, sqle: SQLEnumerableData) -> str:
    """
    Build an insert request for json table or relational table.

    Args:
        command: Command to build.
        sqle: SQLEnumerable with connection, flags, list of commands and a table.

    Returns:
        Request to execute.

    Raises:
        TypeError: Raise when the data had the wrong type or
            Indirect raise by `_build_json_insert`.
        ValueError: Indirect raise by `_build_json_insert`.
    """
    column = command.args.column
    data = command.args.data

    match data:
        case dict():
            return _build_json_insert(data, column, sqle.table)
        case tuple():
            return _build_relational_insert(data, column, sqle.table)
        case list():
            if isinstance(data[0], dict):
                return _build_json_insert(data, column, sqle.table)
            return _build_relational_insert(data, column, sqle.table)
        case str():
            return _build_relational_insert(data, column, sqle.table)
        case _:
            raise TypeError("Data must be type of dict, list, tuple or str.")


def build_update(
    command: Command,
    sqle: SQLEnumerableData,
    built_commands: Set[int],
) -> str:
    """
    Build an update request.

    Args:
        command: Command to build.
        sqle: SQLEnumerable with connection, flags, list of commands and a table.
        built_commands: All commands that have already been built.

    Returns
        Request to execute.

    Raises:
        TooManyReturnValueError: If len of path > 1.
        psycopg.Error: Indirect raise by `build_where`.
        TableError: Indirect raise by `build_where`.
        TypeError: Indirect raise by `build_where`.
        TypeOperatorError: Indirect raise by `build_where`,
            `BaseMagicDotPath._get_number_operator`
            or `BaseMagicDotPath._get_generic_operator`.
    """
    fquery = command.args.fquery  # pylint: disable=duplicate-code
    mdp_w_path = fquery(MagicDotPath(sqle.connection))
    path = get_path(mdp_w_path, sqle)

    if len(path) > 1:
        raise TooManyReturnValueError("Update")

    operand_1 = mdp_w_path.operand_1
    column = operand_1.column
    operand_2 = mdp_w_path.operand_2

    json = len(operand_1.attributes) > 1
    path_for_update = "-".join(operand_1.attributes[1:])

    result = [f"UPDATE {sqle.table} SET {column} ="]

    if json:
        result.append(
            f"""jsonb_set({column}, """
            f"""'{get_update_path(path_for_update)}'::text[], '""",
        )

    match operand_2:
        case str() if not json:
            result.append(f"'{operand_2}'")
        case str() if json:
            result.append(f'"{operand_2}"')
        case _:
            result.append(f"{operand_2}")

    if json:
        result.append("', false)")

    if len(sqle.cmd) > 1:
        result.append(build_where(sqle, built_commands))

    # We use filter with None for the argument __function.
    # If we give None to the first element of filter
    # it will pass all the elements evaluate to false no matter why.
    #
    # We can have None in result if sqle.cmd contains commands
    # which will be evaluated later in build_where()
    return " ".join(filter(None, result))
