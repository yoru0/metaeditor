import pytz
import pandas as pd
import MetaTrader5 as mt5
from datetime import datetime

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

pd.set_option("display.max_columns", 500)  # number of columns to be displayed
pd.set_option("display.width", 1500)  # max table width to display

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
utc_from = datetime(2025, 7, 15, tzinfo=timezone)
utc_to = datetime(2025, 9, 22, tzinfo=timezone)

rates = mt5.copy_rates_range("XAUUSDc", mt5.TIMEFRAME_M1, utc_from, utc_to)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display each element of obtained data in a new line
print("Display obtained data 'as is'")
counter = 0
for rate in rates:
    counter += 1
    if counter <= 10:
        print(rate)

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
rates_frame["time"] = pd.to_datetime(rates_frame["time"], unit="s")


# display data
print("\nDisplay dataframe with data")
print(rates_frame.head(10))

# plot bar chart
