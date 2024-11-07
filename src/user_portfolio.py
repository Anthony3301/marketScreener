from collections import defaultdict
from trade_action import TradeAction

class UserPortfolio:
    def __init__(self):
        # first is total value and second is share amount
        self.positions = defaultdict(lambda : [0,0])
        self.total_value = 0.0
        self.pastValues = []
    
    def add_trade(self, trade: TradeAction):
        if trade.is_buy():
            self.total_value += trade.total_cost
            self.positions[trade.symbol][0] += trade.total_cost
            self.positions[trade.symbol][1] += trade.shares
            
            self.pastValues.append(self.total_value)
        else:
            self.total_value -= self.positions[trade.symbol][0]
            self.total_value += trade.total_value
            self.positions[trade.symbol][1] -= trade.shares
            
            if self.positions[trade.symbol][1] == 0:
                self.positions.pop(trade.symbol)
    
    def __str__(self):
        if not self.positions:
            return "Portfolio is empty"
        
        output = "Current Portfolio:\n"
        output += "================\n"
        for symbol, position in self.positions.items():
            output += f"{symbol}: {position[1]} shares at total value ${position[0]}\n"
        output += f"\nTotal Portfolio Value: ${self.total_value:.2f}"
        return output
    
    def __repr__(self):
        return f"UserPortfolio(positions={dict(self.positions)})"
    
    