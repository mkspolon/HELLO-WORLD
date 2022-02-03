def room3():
    print("\nNow you entered into a maze room, you don't know if have zombies in there!")
    print("There is only two ways, Left or right. What would you do? (1 or 2)")
    print("1). Go left silently.")
    print("2). Go to rigt making noise, Kill the zombies and show your courage!")

    answer = input()
    if answer == "1":
        print("\nNice, you reached somewere safe! Congrats you win the game!")
        play_again()
    elif answer == "2":
        game_over("The zombies was hungry, you couldn't kill them all, they ate you.")
    else:
        game_over("Go and learn how to type a number.")

def room2():
    print("\nThere is a few zombies here.")
    print("Next the zombie is another door.")
    print("They are eating blood of a dead body!")
    print("What would you do? (1 or 2)")
    print("1 - Kill all zombies.")
    print("2 - Go trough the door silently?")

    answer = input(">")
  
    if answer == "1":
        game_over("You killed one zombie and the others zombies killed you.")
    elif answer == "2":
        print("\nPerfect, you got to the door without been noticed, go through it now!")
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
        game_over("The hurrycane damaged the garrage and killed you, Game Over!")
    elif answer == "2":
        print("Right choice, you got into the castel and you are safe from the hurrycane!")
        room2()
    else:
        game_over(answer+" is not valid")


def play_again():
    print("\nDo you want to play again? (y or n)")
    answer = input(">").lower()
    if "y" in answer:
        start()
    else:
        exit()

def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()
    
def start():
    print("\nYou are running away from a killer.")
    print("There is a door to your left and right, which one do you take? (l or r)")
    answer = input(">").lower()
    if "l" in answer:
        room2()
    elif "r" in answer:
        room3()
    else:
        game_over(answer+" is not valid")
    
start()