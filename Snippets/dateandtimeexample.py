#basic date printing
from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day
print (current_year)
print (current_month)
print (current_day)

print ("%02d/%02d/%04d" % (now.day, now.month, now.year))

print ("%02d:%02d:%02d" % (now.hour, now.minute, now.second))

