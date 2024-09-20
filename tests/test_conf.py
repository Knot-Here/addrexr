# tests/test_utils.py

import os
import pytest
from addrexr.utils import get_blockchains

def test_blockchains_file_exists():
    """Test to ensure blockchains.json exists and is loadable."""
    try:
        blockchains = get_blockchains()
        assert isinstance(blockchains, dict), "The blockchains data should be a dictionary."
        assert len(blockchains) > 0, "The blockchains data should not be empty."
    except FileNotFoundError:
        pytest.fail("blockchains.json file was not found.")
    except json.JSONDecodeError:
        pytest.fail("blockchains.json could not be decoded.")

