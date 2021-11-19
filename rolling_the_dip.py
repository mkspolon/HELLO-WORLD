import random
print("Dice Rolling Game")
user_input = []
while user_input !='yes' or user_input !='y':
    user_input = (input("Want to Roll (y/n):"))

    if user_input == 'y':
        d1=random.randint(1,6)
        print(d1)
    else:
        print("end of the game")
        break
    