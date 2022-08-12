from pathlib import Path
import distutils_pytest

def pytest_report_header(config):
    """Add information on the package version used in the tests.
    """
    modpath = Path(distutils_pytest.__file__).resolve().parent
    return [ "distutils-pytest: %s" % (distutils_pytest.__version__),
             "                  %s" % (modpath)]
