import json
from app.adapters.gmail_simple import fetch_inbox_messages

if __name__ == "__main__":
    msgs = fetch_inbox_messages(max_results=10)  # change as needed
    print(f"Fetched {len(msgs)} messages from INBOX\n")
    print("=== Preview of first 5 ===")
    for m in msgs[:5]:
        print(f"From: {m['from']}")
        print(f"Subject: {m['subject']}")
        print(f"Date: {m['date']}")
        print(f"Snippet: {m['snippet']}\n")

    # Full JSON (optional)
    # print(json.dumps(msgs, indent=2, default=str))