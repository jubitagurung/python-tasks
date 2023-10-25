# define the user name and get the name for it
user_name = input("Enter your name:")

vowels = 0
# use the for loop to count vowel in time
for i in user_name:
    if i.lower() in "aeiou":
        vowels += 1
        print(f"Enter the number vowels in your name is {vowels}.")
        

