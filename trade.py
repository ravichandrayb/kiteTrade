from kite_trade import *
from utilities import *
from config import *

# # First Way to Login
# # You can use your Kite app in mobile
# # But You can't login anywhere in 'kite.zerodha.com' website else this session will disconnected

enctoken = "lue3kT4s/l0I9Ikv6MY983ASzmZm6CUwtpvAmrRYJCX1OmiZpbYYjSpSbWl682932iVa5VB9Q3nzGsI0lEIjLYSl3fnJCA/gPvd9NOklKeotHnruja5g9w=="
kite = KiteApp(enctoken=enctoken)
print(kite.margins())
print(kite.orders())
print(kite.positions())

# Get instrument or exchange
#print(kite.instruments())
#print(kite.instruments("NSE"))
#print(kite.instruments("NFO"))

# Get Live Data
#print(kite.ltp("NSE:RELIANCE"))
#print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))
print(kite.quote(["NSE:NIFTY BANK", "NSE:ACC", "NFO:NIFTY22SEPFUT"]))

import datetime
import pandas as pd
instrument_token = 1922049
from_datetime = datetime.datetime.now() - datetime.timedelta(days=7)     # From last & days
#from_datetime = round_to_nearest_lower_15_mins() - datetime.timedelta(minutes = 0);
to_datetime = datetime.datetime.now()
#to_datetime = from_datetime + datetime.timedelta(minutes = 10)
interval = "15minute"

#print(round_to_nearest_lower_15_mins())
#print(from_datetime)
#print(to_datetime)
print(kite.__dict__)
data = kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False)
price_dataframe = pd.DataFrame.from_dict(data)
print(price_dataframe)