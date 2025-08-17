from __future__ import annotations
from pathlib import Path
import os
from typing import List, Dict, Any

from simplegmail import Gmail
from simplegmail.query import construct_query

# We keep OAuth files under backend/credentials/
CREDENTIALS_DIR = Path(__file__).resolve().parent.parent.parent / "credentials"
CLIENT_SECRET = CREDENTIALS_DIR / "client_secret.json"
TOKEN_FILE = CREDENTIALS_DIR / "token.json"

def get_gmail_client() -> Gmail:
    """
    Returns an authenticated Gmail client.
    First run: opens browser for OAuth and writes token.json.
    Subsequent runs: reuses token.json silently.
    """
    # Ensure folder exists (helpful on fresh clones)
    CREDENTIALS_DIR.mkdir(parents=True, exist_ok=True)
    if not CLIENT_SECRET.exists():
        raise FileNotFoundError(
            f"Missing Google OAuth client secret at {CLIENT_SECRET}.\n"
            "Place your client_secret.json in backend/credentials/."
        )

    return Gmail(
        client_secret_file=str(CLIENT_SECRET),
        creds_file=str(TOKEN_FILE),
    )

def fetch_inbox_messages(*, months: int | None = None,
                         max_results: int = 50,
                         primary_only: bool = True) -> List[Dict[str, Any]]:
    """
    Fetch messages from INBOX with a date window.
    Only authentication + fetching (no classification here).
    """
    gmail = get_gmail_client()

    # Default lookback from env or param
    if months is None:
        months = int(os.getenv("GMAIL_LOOKBACK_MONTHS", "1"))

    # simplegmail expects a dict like {"newer_than": (1, "month")}
    base_q = construct_query({"newer_than": (months, "month")})
    # Restrict to Gmail Primary category if requested
    q = f"{base_q} category:primary" if primary_only else base_q

    # simplegmail versions differ: some expect maxResults (camelCase), not max_results
    try:
        messages = gmail.get_messages(query=q, labels=["INBOX"], maxResults=max_results)
    except TypeError:
        # Fallback: older signature without size kwarg; slice in Python
        try:
            messages = gmail.get_messages(query=q, labels=["INBOX"])[:max_results]
        except Exception as e:
            raise RuntimeError(
                "Failed to fetch Gmail messages.\n"
                f"client_secret: {CLIENT_SECRET}\n"
                f"token_file:    {TOKEN_FILE}\n"
                "Tips: (1) Ensure client_secret.json exists. (2) Delete token.json to re-auth. "
                "(3) Run scripts/test_gmail_auth.py to complete OAuth in a browser.\n"
                f"Original error: {e!r}"
            ) from e
    except Exception as e:
        raise RuntimeError(
            "Failed to fetch Gmail messages.\n"
            f"client_secret: {CLIENT_SECRET}\n"
            f"token_file:    {TOKEN_FILE}\n"
            "Tips: (1) Ensure client_secret.json exists. (2) Delete token.json to re-auth. "
            "(3) Run scripts/test_gmail_auth.py to complete OAuth in a browser.\n"
            f"Original error: {e!r}"
        ) from e

    out = []
    for m in messages:
        out.append({
            "id": m.id,
            "thread_id": m.thread_id,
            "date": m.date,                # string from simplegmail
            "from": m.sender,
            "to": getattr(m, "recipient", None),
            "subject": m.subject,
            "snippet": m.snippet,
            # For this step we’re just fetching; no parsing. Prefer plain text if present.
            "body": m.plain if m.plain else (m.html or ""),
        })
    return out