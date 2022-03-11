import pytz
import datetime 
from datetime import timedelta
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

class DateUtility:

    def __init__(self, daydata):
        self.daydata = daydata
        
        
    def convert_dt(self,from_date_TZ, to_date_TZ):
        from_date_TZs = pytz.timezone(from_date_TZ)
        from_dates =datetime.datetime.now(from_date_TZs).strptime(self.daydata, '%Y-%m-%dT%H:%M:%S')
        to_date_TZ = from_dates.astimezone(pytz.timezone(to_date_TZ))
        return to_date_TZ 
    
    
    def add_dt(self, number_of_days):
        # from_date= datetime.datetime.now()
        from_date = datetime.datetime.strptime(self.daydata, '%Y-%m-%dT%H:%M:%S')
        number_of_day = timedelta(days=number_of_days)
        newday =  from_date+number_of_day
        return newday
    

    def diff_day(self, number_of_days):
        from_date = datetime.datetime.strptime(self.daydata, '%Y-%m-%dT%H:%M:%S')
        number_of_day = timedelta(days=number_of_days)
        newday =  from_date-number_of_day
        return newday
    
    
    
    def get_days(self,from_date , to_date):
        from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
        to_dates = datetime.datetime.strptime(to_date, '%Y-%m-%d')
        diff_day = abs(to_dates-from_date)
        return diff_day
    
    
    
    def EPOCH(self):
        return (datetime.datetime.strptime(self.daydata, '%Y-%m-%dT%H:%M:%S') - datetime.datetime(1970, 1, 1)).days
      
      
      
    def excludeWeekend(self, from_date, to_date):
        from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
        to_dates = datetime.datetime.strptime(to_date, '%Y-%m-%d')
        return sum([1 for day in range(1, ( to_dates - from_date).days + 1)
                    if (from_date + datetime.timedelta(day)).weekday() < 5])
        
        
        
    def excluding_holidays(self,from_date, add_days):
        us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())
        y = pd.date_range(start=from_date, end=add_days, freq=us_bd)  
        return len(y)
  

        
    
my = DateUtility("2022-03-18T11:18:10")
print(my.convert_dt('Asia/Kolkata', 'US/Eastern'))
print(my.add_dt(5))
print(my.get_days("2022-03-18","2022-03-11"))
print(my.EPOCH())
print(my.excludeWeekend("2022-01-11","2022-03-10"))
print(my.excluding_holidays("2022-01-11","2022-03-10"))

