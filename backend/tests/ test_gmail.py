

import pytest
import sys
import pathlib

# Ensure the backend/app directory is importable when running `pytest` from backend/
ROOT = pathlib.Path(__file__).resolve().parents[1]
APP_DIR = ROOT / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

# We expect this module to exist soon; the first run may fail (red) until you create it.
from services.gmail_client import connect_gmail

def test_connect_gmail_raises_if_creds_missing():
    """When credentials file is missing, connect_gmail must raise FileNotFoundError."""
    missing = "/tmp/__definitely_missing_gmail_creds__.json"
    with pytest.raises(FileNotFoundError):
        connect_gmail(missing)