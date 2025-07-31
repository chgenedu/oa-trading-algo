# oa-trading-algo
## Trading Algorithm
### Description
This is an exercise to create a trading algorithm. A momentum-based trading algorithm is implemented on QuantConnect.com.

### Trading Thesis
We will allocate our funds among the the following assets: SPY (SPDR S&P 500 ETF Trust), BND (Vanguard Total Bond Market Index Fund), and the stock for a single volatile publicly-traded company (whose symbol is to be loaded from an external file). Momentum of their prices will be used to determine how to reallocated the assets. We have three different allocation options. 
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
The stock symbol for the single volatile publicly-traded company will be stored in a text file on GitHub, and the file will be loaded into the QuantConnect program during run time. The purpose for doing this is to practice the technique of accessing external data source from a QuantConnect program. The individual publicly traded company stock used was AAPL.

Several backtests were done. 
* Backtest1 was run from Aug-1-2007 to Aug-1-2010, with AAPL as the stock.
* Backtest2 was run from Aug-1-2007 to Aug-1-2020, with AAPL as the stock.
For analysis of the trading algorithm, SPY was used as the benchmark.

For additional comparison, one more backtest was performed using SPY in place of AAPL as the stock (so SPY was used for both the market basket fund, and as the proxy for one individual publicly traded company).


### Result
Backtest 1: Aug-1-2007 to Aug-1-2010: Symbol AAPL
![summary-chart1.png](./backtest-report/summary-chart1.png)
![statistics-overview1.png](./backtest-report/statistics-overview1.png)
![KeyCharts1.png](./backtest-report/KeyCharts1.png)

Backtest 2: Aug-1-2007 to Aug-1-2020: Symbol AAPL
![summary-chart2.png](./backtest-report/summary-chart2.png)
![statistics-overview2.png](./backtest-report/statistics-overview2.png)
![KeyCharts2.png](./backtest-report/KeyCharts2.png)

Backtest 3: Aug-1-2007 to Aug-1-2020: Symbol SPY
![summary-chart3.png](./backtest-report/summary-chart3.png)
![statistics-overview3.png](./backtest-report/statistics-overview3.png)
![KeyCharts3.png](./backtest-report/KeyCharts3.png)


### Analysis
For both backtests, the charts for Cumulative Returns show that the proposed algorithm outpaced the SPY Benchmark significantly. 
Additionally, we see that: 
* for Backtest1 (with AAPL) over 3 years, the return was 55% with a Sharpe Ratio of 0.508. 
* for Backtest2 (with AAPL) over 13 years, the return was 725% with a Sharpe Ratio of 0.719.

However, we are doing backtesting knowing that AAPL has performed extremely well in the past, so the choice of this stock for experiment might not be too information for the performance of this trading algorithm. Therefore, we compare against Backtest3 where we use SPY in place of AAPL. We see that:
* for Backtest3 (with SPY in place of AAPL) over 13 years, the return was only 92% with a Sharpe Ratio of 0.52.
From this, we see that the choice of the individual company stock is crucial to the return of the algorithm. Since SPY is significantly less volatile as compared with AAPL, so the return for Backtest3 is significantly less than that of Backtest2 over the the same time period. However, from the Cumulative Returns Chart for Backtest3, we can see that by using SPY in place of AAPL, the returns fluctuation much less than that of Backtest2, which had (temporarily) huge losses during the 2007 financial crisis and during 2020 Covid-19 Pandemic.

### Conclusion







