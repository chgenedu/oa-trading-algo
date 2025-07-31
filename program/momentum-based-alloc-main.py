# Calvin H.
# https://github.com/chgenedu
# July 2025

# region imports
from AlgorithmImports import *
# endregion

class MomentumAllocation(QCAlgorithm):
    def initialize(self):
        text = self.download("https://raw.githubusercontent.com/chgenedu/oa-trading-algo/8403d576252557dee077fd6c90b73b5ae739f0a6/data-source/data.txt")
        self._stock_symbol = text.strip()
        # self._stock_symbol = "AAPL"
        # self._stock_symbol = "INTC"
        # self._stock_symbol = "SPY"
        # self._stock_symbol = "GM"
        # self._stock_symbol = "F"
        self.log("Stock Symbol: " + self._stock_symbol)
        self.debug("Stock Symbol: " + self._stock_symbol)

        self.set_start_date(2007, 8, 1) 
        # self.set_end_date(2010, 8, 1)  
        self.set_end_date(2020, 8, 1)  
        self.set_cash(100000)
        self.add_equity("SPY", Resolution.DAILY)
        self.add_equity("BND", Resolution.DAILY)
        self.add_equity(self._stock_symbol, Resolution.DAILY)

        self.spy_momentum = self.momp("SPY", 30, Resolution.DAILY) 
        self.bond_momentum = self.momp("BND", 30, Resolution.DAILY)
        self.stock_momentum = self.momp(self._stock_symbol, 30, Resolution.DAILY)

        self.set_benchmark("SPY")
        self.set_warm_up(30) 

    def on_data(self, data: Slice):
        if self.is_warming_up:
            return

        portfolio_neutral = [
            PortfolioTarget("SPY", 0.3),  # 30% allocation
            PortfolioTarget("BND", 0.3),   # 30% allocation
            PortfolioTarget(self._stock_symbol, 0)
            # remainder in cash
        ]
        portfolio_stock = [
            PortfolioTarget("SPY", 0.5),  
            PortfolioTarget("BND", 0.2),  
            PortfolioTarget(self._stock_symbol, 0.5)   
        ]
        portfolio_bond = [
            PortfolioTarget("SPY", 0.2),  
            PortfolioTarget("BND", 0.7),  
            PortfolioTarget(self._stock_symbol, 0.2)
        ]

        if not self.portfolio.invested:
            self.set_holdings(portfolio_neutral, liquidate_existing_holdings=True)

        # Limit trading to once a week
        if not self.time.weekday() == 1:
            return

        self.log("spy momentum: " + str(self.spy_momentum.current.value))
        self.log("bnd momentum: " + str(self.bond_momentum.current.value))
        self.log("stock momentum: " + str(self.stock_momentum.current.value))

        if self.spy_momentum.current.value < 0 and \
            self.bond_momentum.current.value < 0 and \
            self.stock_momentum.current.value < 0:
            self.set_holdings(portfolio_neutral, liquidate_existing_holdings=True) 
            # liquidate because unspecified part of holdings are in cash
        if self.stock_momentum.current.value > self.spy_momentum.current.value:
            self.set_holdings(portfolio_stock, liquidate_existing_holdings=False)    
        elif self.bond_momentum.current.value > self.spy_momentum.current.value:
            self.set_holdings(portfolio_bond, liquidate_existing_holdings=False)            
        else:
            pass

