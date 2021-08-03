import os
from pathlib import Path

import click

# project root directory.
BASE_DIR = Path(__file__).resolve().parent.parent


@click.command()
def test():
    """
    runs the test suite.
    """
    import pytest
    
    exit(pytest.main(
        [os.path.join(BASE_DIR, "tests")]
    ))
