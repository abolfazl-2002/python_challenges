# print the calendar of a given month and year

import calendar
from datetime import datetime

y = datetime.now().year # get current year
m = datetime.now().month # get current month

c = calendar.month(y,m) # get current month calander

print(c)