#get the value for userinput score
score = int(input("Enter your score:"))
# check the score and assign with the message
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score <= 60:
    print("F")
else:
    print("invalid input")