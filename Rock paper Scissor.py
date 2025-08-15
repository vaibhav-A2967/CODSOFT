import random
choices=["rock","paper","scissors"]
while True:
    print("--Enter quit to finish--")
    player=input("Enter your Choice:(rock,paper,scissors)")
    if player.lower()=="quit":
        print("Thank you!")
        break
    elif player not in choices:
        print("Invalid choice. Try again!")
        continue
    else:
        comp=random.choice(choices)
        print("\n",comp,"is the choice of computer!")

        if player==comp:
            print("Draw the Match!")
        elif ((player=="rock" and comp=="scissors") or (player=="paper" and comp=="rock") or (player=="scissors" and comp=="paper")):
            print("you Won!:)")
        else:
            print("you lose!:(")
