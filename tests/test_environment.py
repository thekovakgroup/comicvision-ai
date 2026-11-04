
import sys


def test_python_version():
    """Verify that Python 3.11 or newer is installed."""
    assert sys.version_info >= (3, 11)


def test_virtual_environment():
    """Verify that Python is running inside a virtual environment."""
    assert sys.prefix != sys.base_prefix
