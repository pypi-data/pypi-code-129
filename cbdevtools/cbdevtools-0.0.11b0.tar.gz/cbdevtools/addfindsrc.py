#!/usr/bin/env python3

###
# This module simplifies the import of the dev source dir of a project.
###


from pathlib import Path
import sys


###
# prototype::
#     file    : just use the magic constant ``__file__`` when calling
#               this function.
#     project : the name of the project
#
#     :return: the path of the project ¨dir.
#
#
# warning::
#     The ¨dir of the project must contain the file path::``__file__``.
###
def addfindsrc(
    file   : str,
    project: str,
) -> Path:
    project_dir = Path(file).parent
    rootdir     = Path('/')

    while(
        project_dir != rootdir
        and
        project_dir.name != project
    ):
        project_dir = project_dir.parent

    assert project_dir.name == project, \
          (
            'call the script from a working directory '
            'containing the project dir.'
          )

    sys.path.append(str(project_dir))

    return project_dir
