# oa-trading-algo
## Trading Algorithm
### Description
This is an exercise to create a trading algorithm. A momentum-based trading algorithm is implemented on QuantConnect.com.

### Trading Thesis
We will allocate our funds among the the following assets: SPY (SPDR S&P 500 ETF Trust), BND (Vanguard Total Bond Market Index Fund), and the stock for a publicly-traded company (to be determined by the information in an external file). Momentum of their prices will be used to determine how to reallocated the assets. We have three different allocation options. 
* Neutral (30% SPY, 30% BND, 40% cash)
* Stock focused (50% SPY, 20% BND, 50% stock)
* Bond focused (20% SPY, 70% BND, 20% stock)

To begin, we will allocate the assets into the Neutral allocation. We will use 30-day momentum indicators for all three assets as signals to decide who to reallocate the assets. 
The following is decision rules for reallocation.
* If the indicators are all negative, we are assuming the market is risky, so we will go into Neutral.
* If stock's momentum is higher than SPY, we will be stock focused.
* If Bond's is higher than SPY's momentum, we will be bond focused.
* Otherwise, we will do nothing.  

### Experiment
The stock symbol for the publicly-traded company will be stored in a text file on GitHub. The purpose for doing this is to practice accessing external data source from a QuantConnect program. 

### Result
