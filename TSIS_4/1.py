from datetime import datetime, timedelta

date = datetime.now()
result = date - timedelta(days=5)

print(date.strftime('%Y-%m-%d'))
print(result.strftime('%Y-%m-%d'))
