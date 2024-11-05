import re
from datetime import datetime

class TradeAction:
    def __init__(self, raw_text):
        """
        Initialize a TradeAction by parsing raw text input.

        :param raw_text: The raw string containing trade details.
        """
        # Custom parsing to extract trade details from the raw text
        self.trade_type = self._parse_trade_type(raw_text)
        self.symbol = self._parse_field(raw_text, r"Symbol:\s\*(.*?)\*")
        
        # Parse shares as integer
        shares_str = self._parse_field(raw_text, r"Shares:\s\*(\d+)\*")
        self.shares = int(shares_str) if shares_str else None
        
        # Parse average price, handling optional "US" or "USD$" prefix and commas
        avg_price_str = self._parse_currency_field(raw_text, r"Average price:\s\*\$?(US|USD\$)?\s?(.*?)\*")
        self.avg_price = float(avg_price_str) if avg_price_str else None
        
        # Check for "Total cost" (buy) or "Total value" (sell), handle optional "US" or "USD$" prefix and commas
        total_cost_str = self._parse_currency_field(raw_text, r"Total cost:\s\*\$?(US|USD\$)?\s?(.*?)\*")
        total_value_str = self._parse_currency_field(raw_text, r"Total value:\s\*\$?(US|USD\$)?\s?(.*?)\*")
        
        # Set the values based on whether it's a buy or sell action
        self.total_cost = float(total_cost_str) if total_cost_str else None
        self.total_value = float(total_value_str) if total_value_str else None
        
        # Parse and store time as datetime
        self.time = self._parse_time(self._parse_field(raw_text, r"Time:\s\*(.*?)\*"))

    def _parse_field(self, text, pattern):
        """
        Extract a field using a regex pattern.

        :param text: The raw text to search.
        :param pattern: The regex pattern to find the field.
        :return: The matched value as a string.
        """
        match = re.search(pattern, text)
        return match.group(1).strip() if match else None

    def _parse_currency_field(self, text, pattern):
        """
        Extract a currency field, handling optional "US" or "USD$" prefix,
        and remove any commas or dollar signs.

        :param text: The raw text to search.
        :param pattern: The regex pattern to find the field.
        :return: The matched currency value as a cleaned string.
        """
        match = re.search(pattern, text)
        if match:
            return match.group(2).replace(',', '').replace('$', '').strip()
        return None

    def _parse_trade_type(self, text):
        """
        Extracts the action type (Buy or Sell) from the Type field in raw text.

        :param text: The raw text to search.
        :return: 'Buy' or 'Sell' if found; otherwise, None.
        """
        match = re.search(r"Type:\s\*Market\*\s\*(Buy|Sell)\*", text, re.IGNORECASE)
        return match.group(1) if match else None

    def _parse_time(self, time_str):
        """
        Convert time string to datetime object.

        :param time_str: The time as a string.
        :return: Parsed datetime object or original string if parsing fails.
        """
        try:
            return datetime.strptime(time_str, "%B %d, %Y %H:%M %Z")
        except ValueError:
            return time_str  # Return the original string if parsing fails

    def __str__(self):
        """
        Returns a string representation of the trade details.
        """
        return (f"Trade Action: {self.trade_type}\n"
                f"Symbol: {self.symbol}\n"
                f"Shares: {self.shares}\n"
                f"Average Price: ${self.avg_price}\n"
                f"{'Total Cost' if self.total_cost is not None else 'Total Value'}: "
                f"${self.total_cost if self.total_cost is not None else self.total_value}\n"
                f"Time: {self.time}\n")

    def calculate_total_value(self):
        """
        Calculate the total value of the trade based on shares and average price.
        """
        return self.shares * self.avg_price if self.shares and self.avg_price else None

    def is_buy(self):
        """
        Check if the trade is a buy action.
        """
        return self.trade_type.lower() == 'buy' if self.trade_type else False

    def is_sell(self):
        """
        Check if the trade is a sell action.
        """
        return self.trade_type.lower() == 'sell' if self.trade_type else False