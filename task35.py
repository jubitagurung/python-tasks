#define the vars as day and get userinput for day
day = input("Enter the day of the week:")
#conver the input to lowercase
day = day.lower() 
#check the day and display it with message
if  day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday":
    print("weekdays")
elif day == "Friday":
    print("TGIF")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("invalid input")