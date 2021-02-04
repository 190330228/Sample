import datetime
dt = datetime.datetime.now()
time = dt.strftime("%H:%M:%S")
to = datetime.date.today()
print("The current time is ",time)
print("The current Date is ",to)