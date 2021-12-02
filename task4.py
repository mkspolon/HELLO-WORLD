def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()

def play_again():
    print("\nDo you want to play again? (y or n)")
    answer = input(">").lower()
    if "y" in answer:
        start()
    else:
        exit()

def room3():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")

answer = input()
if answer == "1":
    print("\nNice, you reached somewere safe! Congrats you win the game!")
    play_again()
elif answer == "2":
    game_over("The monster was hungry, he/it ate you.")
else:
    game_over("Go and learn how to type a number.")

def room2():
    print("\nThere is a bear here.")
    print("Behind the bear is another door.")
    print("The bear is eating tasty honey!")
    print("What would you do? (1 or 2)")
    print("1 - Take the honey.")
    print("2 - Taunt the bear.")

answer = input(">")
  
if answer == "1":
    game_over("The bear killed you.")
elif answer == "2":
    print("\nYour Good time, the bear moved from the door. You can go through it now!")
    room3()
else:
    game_over(answer+" is not valid")

def room1():
    print("\n you are on the street and a hurricane is coming")
    print("you need to get into somewere safe to protect yourself")
    print("there is a garage door and a castel door with one would you go?")
    print("1 - Garage door:\n 2 - Castel door?")

answer = input()

if answer == "1":
    game_over("The hurrycane damaged the garrage, Game Over!")
elif answer == "2":
    print("Right choice, you got into the castel and you are safe from the hurrycane!")
    room2()
else:
    game_over(answer+" is not valid")

def start():
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and right, which one do you take? (l or r)")
    answer = input(">").lower()
    if "l" in answer:
        room2()
    elif "r" in answer:
        room3()
    else:
        game_over(answer+" is not valid")

start()