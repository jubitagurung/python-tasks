#define the user number and get the number
user_number = int(input("Enter your number:"))

factorial = 1
#use a for loop
for i in range(1, user_number + 1):
    factorial *= i
    
    print("the factorial number is:",user_number)
    