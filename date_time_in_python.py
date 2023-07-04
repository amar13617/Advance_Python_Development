from datetime import datetime, timezone, timedelta

#print(datetime.now())

#print(datetime.now(timezone.utc))
today = datetime.now(timezone.utc)
tommorrow = today + timedelta(days=1)
#print(today)
#print(tommorrow)

print(today.strftime('%d-%m-%Y %H:%M'))


from datetime import datetime

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time

print(user_date)