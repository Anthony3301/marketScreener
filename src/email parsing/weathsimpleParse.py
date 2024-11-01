import imaplib
import email
from email.policy import default
from dotenv import load_dotenv
import os

import mailbox
import re

load_dotenv()


mbox_file_path = os.getenv('TRADE_EMAIL_PATH')

start_pattern = r"Your order has been filled Account"
end_pattern = r"\*\* \(  \)"

matched_content = []
with open(mbox_file_path, 'r', encoding='utf-8', errors='ignore') as file:
    file_content = file.read()
    matches = re.findall(f"{start_pattern}.*?{end_pattern}", file_content, re.DOTALL)
    matched_content.extend(matches)

if matched_content:
    for i, content in enumerate(matched_content, 1):
        print(f"Match {i}:")
        print(content)
        print("\n" + "="*40 + "\n")
else:
    print("No matches found.")

