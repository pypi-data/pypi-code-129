# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida-core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
"""
AiiDA is a flexible and scalable informatics' infrastructure to manage,
preserve, and disseminate the simulations, data, and workflows of
modern-day computational science.

Able to store the full provenance of each object, and based on a
tailored database built for efficient data mining of heterogeneous results,
AiiDA gives the user the ability to interact seamlessly with any number of
remote HPC resources and codes, thanks to its flexible plugin interface
and workflow engine for the automation of complex sequences of simulations.

More information at http://www.aiida.net
"""
import warnings

from aiida.common.log import configure_logging
from aiida.common.warnings import AiidaDeprecationWarning
from aiida.manage.configuration import get_config_option, get_profile, load_profile

__copyright__ = (
    'Copyright (c), This file is part of the AiiDA platform. '
    'For further information please visit http://www.aiida.net/. All rights reserved.'
)
__license__ = 'MIT license, see LICENSE.txt file.'
__version__ = '1.6.9'
__authors__ = 'The AiiDA team.'
__paper__ = (
    'S. P. Huber et al., "AiiDA 1.0, a scalable computational infrastructure for automated reproducible workflows and '
    'data provenance", Scientific Data 7, 300 (2020); https://doi.org/10.1038/s41597-020-00638-4'
)
__paper_short__ = 'S. P. Huber et al., Scientific Data 7, 300 (2020).'


def load_dbenv(profile=None):
    """Alias for `load_dbenv` from `aiida.backends.utils`

    :param profile: name of the profile to load
    :type profile: str

    .. deprecated:: 1.0.0
        Will be removed in `v2.0.0`, use :func:`aiida.manage.configuration.load_profile` instead.
    """
    warnings.warn('function is deprecated, use `load_profile` instead', AiidaDeprecationWarning)  # pylint: disable=no-member
    current_profile = get_profile()
    from aiida.common import InvalidOperation

    if current_profile:
        raise InvalidOperation('You cannot call load_dbenv multiple times!')

    load_profile(profile)


def try_load_dbenv(profile=None):
    """Run `load_dbenv` unless the dbenv has already been loaded.

    :param profile: name of the profile to load
    :type profile: str

    :returns: whether profile was loaded
    :rtype: bool


    .. deprecated:: 1.0.0
        Will be removed in `v2.0.0`, use :func:`aiida.manage.configuration.load_profile` instead.
    """
    warnings.warn('function is deprecated, use `load_profile` instead', AiidaDeprecationWarning)  # pylint: disable=no-member
    if not is_dbenv_loaded():
        load_dbenv(profile)
        return True
    return False


def is_dbenv_loaded():
    """Determine whether database environment is already loaded.

    :rtype: bool

    .. deprecated:: 1.0.0
        Will be removed in `v2.0.0`, use :func:`aiida.manage.configuration.load_profile` instead.
    """
    warnings.warn('function is deprecated, use `load_profile` instead', AiidaDeprecationWarning)  # pylint: disable=no-member
    return get_profile() is not None


def get_strict_version():
    """
    Return a distutils StrictVersion instance with the current distribution version

    :returns: StrictVersion instance with the current version
    :rtype: :class:`!distutils.version.StrictVersion`
    """
    from distutils.version import StrictVersion
    return StrictVersion(__version__)


def get_version():
    """
    Return the current AiiDA distribution version

    :returns: the current version
    :rtype: str
    """
    return __version__


def _get_raw_file_header():
    """
    Get the default header for source AiiDA source code files.
    Note: is not preceded by comment character.

    :return: default AiiDA source file header
    :rtype: str
    """
    return f"""This file has been created with AiiDA v. {__version__}
If you use AiiDA for publication purposes, please cite:
{__paper__}
"""


def get_file_header(comment_char='# '):
    """
    Get the default header for source AiiDA source code files.

    .. note::

        Prepend by comment character.

    :param comment_char: string put in front of each line
    :type comment_char: str

    :return: default AiiDA source file header
    :rtype: str
    """
    lines = _get_raw_file_header().splitlines()
    return '\n'.join(f'{comment_char}{line}' for line in lines)
