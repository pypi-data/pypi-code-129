# -*- coding: ascii -*-


"""Pragmatic.Pragmatic: provides entry point main()."""


__version__ = "0.0.13"

from . import Stuff
from .Registry import Registry
from .ArgParser import ParseArgs, Test
from .GetRelease import Get

def Update():
	Get('LLVM', 'llvm-0.1')
	Get('PragmaticPlugin', '0.1')


def Main():
	print(f"Running pragmatic version {__version__}.")

	ParseArgs()