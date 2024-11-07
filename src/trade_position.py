from trade_action import TradeAction
from collections import defaultdict

class TradePosition:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        
        # key = price, val = number of shares at price
        self.shareSpread = defaultdict(int)
    
    def init(self, trade: TradeAction):
        self.shareSpread[trade.avg_price] += trade.shares
    
    def addTrade(self, trade: TradeAction):
        self.shareSpread[trade.avg_price] += (-1 if trade.is_buy() else 1) * trade.shares
    
    def __str__(self):
        return f"{self.symbol}: {self.shareSpread}"
    
    def __repr__(self):
        return f"TradePosition(symbol={self.symbol}, shares={self.shares})"