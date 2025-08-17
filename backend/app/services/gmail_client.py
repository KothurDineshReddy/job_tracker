# backend/app/services/gmail_client.py
from pathlib import Path

def connect_gmail(credentials_path: str):
    """
    Minimal placeholder. For now, only validates that the credentials file exists.
    Real Gmail OAuth logic will come later behind this interface.
    """
    p = Path(credentials_path)
    if not p.exists():
        raise FileNotFoundError(f"Credentials file not found: {credentials_path}")
    return True