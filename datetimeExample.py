from datetime import datetime

datetime_obj = datetime.now()
#print(datetime_obj)

stringDate = datetime_obj.strftime('%m / %d / %Y')
print(stringDate)

another_date = datetime.strptime('02-08-2021','%m-%d-%Y')
print(another_date)