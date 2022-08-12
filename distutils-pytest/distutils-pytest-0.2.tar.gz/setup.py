"""distutils-pytest - Call pytest from a setup.py script

This Python module implements a `test` command for a `setup.py`
script.  The command will call `pytest`_ to run your package's test
suite.

.. _pytest: http://pytest.org/
"""

import setuptools
from setuptools import setup
import setuptools.command.build_py
import distutils.command.sdist
import distutils.file_util
from distutils import log
from glob import glob
import os
from pathlib import Path
from stat import ST_ATIME, ST_MTIME, ST_MODE, S_IMODE
import string
import distutils_pytest
try:
    import setuptools_scm
    version = setuptools_scm.get_version()
except (ImportError, LookupError):
    try:
        import _meta
        version = _meta.__version__
    except ImportError:
        log.warn("warning: cannot determine version number")
        version = "UNKNOWN"

docstring = __doc__

class copy_file_mixin:
    """Distutils copy_file() mixin.

    Inject a custom version version of the copy_file() method that
    does some substitutions on the fly into distutils command class
    hierarchy.
    """
    Subst_srcs = {"distutils_pytest.py"}
    Subst = {'DOC': docstring, 'VERSION': version}
    def copy_file(self, infile, outfile,
                  preserve_mode=1, preserve_times=1, link=None, level=1):
        if infile in self.Subst_srcs:
            infile = Path(infile)
            outfile = Path(outfile)
            if outfile.name == infile.name:
                log.info("copying (with substitutions) %s -> %s",
                         infile, outfile.parent)
            else:
                log.info("copying (with substitutions) %s -> %s",
                         infile, outfile)
            if not self.dry_run:
                st = infile.stat()
                try:
                    outfile.unlink()
                except FileNotFoundError:
                    pass
                with infile.open("rt") as sf, outfile.open("wt") as df:
                    df.write(string.Template(sf.read()).substitute(self.Subst))
                if preserve_times:
                    os.utime(str(outfile), (st[ST_ATIME], st[ST_MTIME]))
                if preserve_mode:
                    outfile.chmod(S_IMODE(st[ST_MODE]))
            return (str(outfile), 1)
        else:
            return distutils.file_util.copy_file(infile, outfile,
                                                 preserve_mode, preserve_times,
                                                 not self.force, link,
                                                 dry_run=self.dry_run)

class meta(setuptools.Command):
    description = "generate meta files"
    user_options = []
    meta_template = '''
__version__ = "%(version)s"
'''
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        values = {
            'version': self.distribution.get_version(),
        }
        with Path("_meta.py").open("wt") as f:
            print(self.meta_template % values, file=f)

# Note: Do not use setuptools for making the source distribution,
# rather use the good old distutils instead.
# Rationale: https://rhodesmill.org/brandon/2009/eby-magic/
class sdist(copy_file_mixin, distutils.command.sdist.sdist):
    def run(self):
        self.run_command('meta')
        super().run()
        subst = {
            "version": self.distribution.get_version(),
            "url": self.distribution.get_url(),
            "description": self.distribution.get_description(),
            "long_description": self.distribution.get_long_description(),
        }
        for spec in glob("*.spec"):
            with Path(spec).open('rt') as inf:
                with Path(self.dist_dir, spec).open('wt') as outf:
                    outf.write(string.Template(inf.read()).substitute(subst))

class build_py(copy_file_mixin, setuptools.command.build_py.build_py):
    def run(self):
        self.run_command('meta')
        super().run()


with Path("README.rst").open("rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name = "distutils-pytest",
    version = version,
    description = "Call pytest from a setup.py script",
    long_description = readme,
    url = "https://github.com/RKrahl/distutils-pytest",
    author = "Rolf Krahl",
    author_email = "rolf@rotkraut.de",
    license = "Apache-2.0",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Build Tools",
    ],
    py_modules = ["distutils_pytest"],
    install_requires = ["pytest"],
    python_requires = ">=3.4",
    cmdclass = dict(distutils_pytest.cmdclass,
                    build_py=build_py, sdist=sdist, meta=meta),
)
