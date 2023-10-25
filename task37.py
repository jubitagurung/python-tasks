# get the value for user input of month
month = input("Enter the month:")
month = month.lower()
#check the months and assign it with season
if month == "january" or month == "february" or month == "march" or month == "april" or month == "may":
    print("spring")
    
elif month == "june" or month == "july" or month == " august":
    print("summer")
    
elif month == "september" or month == "october" or month == "november":
    print("winter")
    
else:
    print("invalid month")