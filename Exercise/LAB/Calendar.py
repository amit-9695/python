import calendar
y=int(input("Enter a Year: "))
m=1
print("\n******** CALENDAR ********")
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12:
    cal.prmonth(y,i)
    i+=1
