user_inputs = []
for i in range(3):
    
    num = input(f"Enter number {i+1}: ")
    
    user_inputs.append(int(num))


def is_even(array):
    for x in array:
         if x % 2 != 0:
             return False
    return True
result = is_even(user_inputs)
print(f"All numbers are even: {result}")











    

