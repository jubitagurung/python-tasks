# define user name and get the number from user
user_number = int(input("Enter your number:"))

factorial = 1
if user_number < 0:
    print("sorry, this factorial does not exist")
elif user_number == 0:
    print("factorial of 0 is 1")
else:
#use while loop
    while user_number < 0:
         factorial *= user_number
         user_number -= 1
    print("the number factorial is:", user_number)
         