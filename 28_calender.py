import calendar
########my code
year=int(input("Enter year: "))
month=int(input("Enter month: "))
# cal=calendar.month(year,month)
# print(cal)

####extra learning
#print(calendar.month(2000,12))
#print("----------------------")
#print(calendar.calendar(2025))

# Extra useful info first_day, 
first_day, num_days = calendar.monthrange(year, month) 
print(f"First weekday (0=Mon): {first_day}") 
print(f"Number of days: {num_days}") 
# Matrix form 
print("\nWeek matrix:") 
for week in calendar.monthcalendar(year, month): 
    print(week)