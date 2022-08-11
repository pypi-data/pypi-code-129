"""
Class decorators for docstrings.

These classes are used for appending and substituting docstrings to
classes and methods.  They were copied from pandas.pandas.utils._decorators.py
"""

from typing import Any, Callable, Dict, Optional, TypeVar

FuncType = Callable[..., Any]
F = TypeVar("F", bound=FuncType)


def create_shared_doc_vars():
    """
    Creates variables that will be used to keep track of shared documents
    within a package.

    These should be imported (instead of creating) to modules that have any
    classes that inherit from objects defined in other modules.

    Returns
    -------
    _shared_docs : dict

    _shared_doc_kwargs : dict
        The dictionary that holds the shared arguments among a package

    See also
    --------
    utils.decorators.Appender

    Notes
    -----

    Examples
    --------
    from utils.decorators import Appender

    # -----------------------------------------------------------------------------

    _shared_docs, _shared_doc_kwargs = create_shared_doc_vars()
    _shared_doc_kwargs['shared_arg'] = \"""shared_arg : str
        The entire filename, including the path and
        filename.\"""

    def myClass():

        _shared_docs["my_static_method"] = \"""

            Parameters
            ----------
            %(shared_arg)s

            \"""

        @staticmethod
        Appender()
        def my_static_method(shared_arg)
    """

    # A dictionary of common keyword arguments to methods
    _shared_doc_kwargs: Dict[str, str] = dict()

    # A Dictionary for holding docstrings for classes and methods
    _shared_docs: Dict[str, str] = dict()

    return _shared_docs, _shared_doc_kwargs
