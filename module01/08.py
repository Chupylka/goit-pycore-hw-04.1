# ВИВЕСТИ ВСІ ДАННІ ЯКІ Є В ПРОМІЖКУ ЗАЗНАЧЕНОГО ЧАСУ

from datetime import date, timedelta


start_date = date(year=2023, day=12, month=10)
end_date = date(year=2023, day=25, month=10)
delta = end_date - start_date
days = delta.days + 1

for i in range(days):
    res = start_date + timedelta(days=i)
print(res)




# РОБОТА З ЧАСОВИМИ ПОЯСАМИ
# >>>poland_zone = pytz.timezone("Poland")
# >>>poland_zone
# >>> from datetime import datetime
# >>> datetime.now(tz=poland_zone)

#pytz
# pip(?3) install pytz

# import pytz # type: ignore

#from datetime import datetime

#d = datetime.now()

#iso = d.isoformat(sep="T")
#print(iso)

#iso = d.timestamp()
#print(iso)

#__________________________________________________

#from datetime import datetime, timezone

#current_time_utc = datetime.now(timezone.utc)
#print(current_time_utc)

#__________________________________________________

#import time

#x = 0
#while x < 10:
#    print("Tutor Joe's")
#    time.sleep(2)
#    x = x + 1