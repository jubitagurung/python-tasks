# define the user name and get the name from user
user_name = input("Enter your name:")
#check whether it has vowels and count it
vowels = ["a","e","i","o","u"]

count = 0

i = 0
while i < len(user_name):
    if user_name [i].lower() in vowels:
        count += 1
        
    i += 1
    print("numbers of vowel in your name:", count)
        

