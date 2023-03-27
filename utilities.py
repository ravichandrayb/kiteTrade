from datetime import datetime, timedelta
import math

def getOptionPriceForTheDay(day,hour):
    capital_day = day.capitalize()
    day_values = {
        "MONDAY" : 200,
        "TUESDAY" : 180,
        "WEDNSDAY" : 150,
        "THURSDAY" : 100,
        "FRIDAY" : 250,
        }
    if capital_day != "THURSDAY" :
        return day_values.capital_day
    else :
        if hour > 12 :
            return 60
        else :
            return 100
def take_closest(option_price_list, option_value_for_the_day):
	min(option_price_list, key=lambda x:abs(x- option_value_for_the_day))

def get_nearest_hour(t):
    if t.minute > 30 :
        t.replace(second=0, microsecond=0, minute=0, hour=t.hour+1)
        return t.hour
    else:
        t.replace(second=0, microsecond=0, minute=0)
        return(t.hour)


def round_to_nearest_lower_15_mins(dt = datetime(2023, 1, 13, 12, 15, 0), delta = timedelta(minutes=15)):
    return datetime.min + math.floor((dt - datetime.min) / delta) * delta
