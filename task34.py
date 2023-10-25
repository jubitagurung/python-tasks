#get userinput for the temperature
temperature = int(input("Enter the temperature:"))
#check the temperature and assign each point
if temperature >= 100:
    print("Boiling")
elif temperature >= 32:
    print("Liquid")
elif temperature <= 32:
    print("Freezing")

