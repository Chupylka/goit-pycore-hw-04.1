from datetime import datetime

#d = datetime(year=2024, month=10, day=12, hour=22, minute=33)
#print(d)

   # print(datetime.now())
   # print(datetime.today())
   # print(date.today()) 

# %Y: 4-digit year
# %y: 2-digit year
# %m: 2-digit mon (01-12)
# %d: 2-digit day of the mon (01-12)
# %H: 2-digit h (00-23)
# %M: 2-digit m (00-59)
# %S: 2-digit s (00-59)


d = "12-10-2023"

d2 = datetime.strptime(d, "%d-%m-%Y")
#print(type(d2))

d3 = d2.strftime("%d %B %Y")
print(d3)
print(type(d3))

# strprime -> string parse time (перетворити з рядка в обєкт в datetime) 
# strtyime ->> string format time (перетворити з datetime в рядок)
