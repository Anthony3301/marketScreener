import os
import re
from dotenv import load_dotenv
from trade_action import TradeAction

load_dotenv()
def extract_trade_actions(mbox_file_path):
    """
    Reads an mbox file, extracts trade details, and returns a list of TradeAction objects.

    :param mbox_file_path: Path to the mbox file.
    :return: List of TradeAction objects parsed from the file.
    """
    mbox_file_path = os.getenv('TRADE_EMAIL_PATH')
    trade_actions = extract_trade_actions(mbox_file_path)
    
    start_pattern = r"Your order has been filled Account"
    end_pattern = r"\*\* \(  \)"

    matched_content = []
    trade_actions = []
    
    with open(mbox_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        file_content = file.read()
        matches = re.findall(f"{start_pattern}.*?{end_pattern}", file_content, re.DOTALL)
        matched_content.extend(matches)

    for content in matched_content:
        trade_actions.append(TradeAction(content))

    return trade_actions