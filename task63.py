user_inputs = []
for i in range(3):
    user_inputs.append(int(input(f"Enter number {i+1}: ")))
    
    def is_even(user_inputs):
         for num in user_inputs:
            if num % 2 == 0:
                print(f"{num} is even")
            else:
                 print(f"{num} is odd")

