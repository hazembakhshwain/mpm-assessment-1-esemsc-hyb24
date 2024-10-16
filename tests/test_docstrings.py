from pydocstyle import check
from pathlib import Path


def test_docstrings():
    """Test that all modules follow PEP 257 docstring conventions."""
    source_dir = Path(__file__).resolve().parent.parent / "acsefunctions"
    result = list(check([str(source_dir)]))
    assert not result, "Some docstrings do not follow PEP 257 standards."
