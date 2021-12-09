import random

print("Dice Rolling Game")
user_input = input("Want to Roll (y/n):")

while user_input =='y':
    d1=random.randint(1,6)
    print(d1)
    user_input = (input("Want to Roll (y/n):"))

    if user_input == 'y':
        continue        
    else:
        print("end of the game")
        break
    