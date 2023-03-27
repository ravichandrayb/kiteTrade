from kite_trade import *
from utilities import *
from config import *
import pandas as pd
import pandas_ta as ta
import datetime

enctoken = get_enctoken(user_id, password, twofa)
kite = KiteApp(enctoken=enctoken)
# Create a DataFrame so 'ta' can be used.
df = pd.DataFrame()

instrument_token = 1922049

from_datetime = datetime.datetime.now() - datetime.timedelta(days=7)     # From last & days
#from_datetime = round_to_nearest_lower_15_mins() - datetime.timedelta(minutes = 0);
to_datetime = datetime.datetime.now()

# Help about this, 'ta', extension
help(df.ta)

# List of all indicators
df.ta.indicators()

interval = "15minute"

# Help about an indicator such as bbands
print(help(ta.bbands))

data = kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False)
price_dataframe = pd.DataFrame.from_dict(data)
interval = "15minute"

ta.bbands(df.close, length=None, std=None, mamode=None, offset=None)
