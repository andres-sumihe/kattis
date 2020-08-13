import datetime
year = 2009
day, month = map(int, input().split())
answer = datetime.date(year, month, day)
print(answer.strftime("%A"))
