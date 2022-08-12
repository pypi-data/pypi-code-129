from pathlib import Path

def test_import():
    """Check that importing the module works.
    """
    import distutils_pytest
    modpath = Path(distutils_pytest.__file__).resolve().parent
    print("version: %s" % distutils_pytest.__version__)
    print("module path: %s" % modpath)
