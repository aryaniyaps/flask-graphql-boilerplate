import os
from pathlib import Path

import click

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_PATH = os.path.join(BASE_DIR, "tests")


@click.command()
def test():
    """
    runs the test suite.
    """
    import pytest
    
    exit(pytest.main(TEST_PATH, "--verbose"))
