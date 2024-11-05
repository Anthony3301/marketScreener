from dotenv import load_dotenv
from polygon import RESTClient
import os
import sys
from pathlib import Path

# Add the email parsing directory to the Python path
sys.path.append(str(Path(__file__).parent / 'email parsing'))
from weathsimpleParse import extract_trade_actions # type: ignore

sys.path.append(str(Path(__file__).parent / 'portfolio'))
from user_portfolio import UserPortfolio # type: ignore
from trade_position import TradePosition # type: ignore

load_dotenv()
polygon_key = os.getenv("POLYGON_KEY")
polygon_client = RESTClient(api_key=polygon_key)

# Initialize user portfolio
portfolio = UserPortfolio()

# Get trade actions from email
trade_actions = extract_trade_actions(os.getenv('TRADE_EMAIL_PATH'))

# Process each trade action
for trade in trade_actions:
    portfolio.add_trade(trade)

# Print the portfolio
print(portfolio)


