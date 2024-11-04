from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0<= days_until_birthday <= 7:
            if birthday_this_year.weekday() == 5:
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str})
            
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]
    
upcoming_birthdays = get_upcoming_birthdays(users)
print(f"Happy birthday 'John Doe'!", '1985.01.23')
print(f"Happy birthday 'Jane Smith'!", '1990.01.27')