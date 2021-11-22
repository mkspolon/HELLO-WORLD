import random

num = random.randint(1, 10)
gess = None
while gess != num:
    gess = input ("Gess a number between 1 and 10: ")
    gess = int(gess)
    if gess == num:
        print("Congratulations, you won!")
        break
    else:
        print("try again.")