# ask user to input the name
name = input("Enter your name:").capitalize()
print(f"Hello {name}! Welcome.. Would you like to proceed and play the game?")
answer = input("Please enter (yes/no):").upper().strip()
if answer == "YES":
    answer = input("You are at cross roads pick path A or B....").upper().strip()
    if answer == "A":
        print("You entered a jungle!")
        answer1 = input("you have to pick a means to get to the other side of the jungle, pick A or B:").upper().strip()
        if answer1 == "A":
            print("You choose to walk, it's dangerous you have to pick a weapon")
            weapon = input("Choose weapon A or B:").upper().strip()
            if weapon == "A":
                print("YOU WIN! You choose a gun. This will help you get to the other side of the jungle")
            elif weapon == "B":
                print("YOU LOOSE! You choose an axe. Sorry but monsters will devour you.")
            else:
                print("Invalid input! YOU LOOSE")
        elif answer1 == "B":
            print("YOU WIN! You choose a Land-cruiser. It will get you to the other side of the jungle.")
        else:
            print("Invalid input! YOU LOOSE")
    elif answer == "B":
        print("You are now at the sea!")
        answer2 = input("Choose a means to get you to the island:").upper().strip()
        if answer2 == "A":
            print("YOU LOOSE!' You chose to swim. The ocean is very risky. ")
        elif answer2 == "B":
            print("You chose a motorboat.YOU WIN! It will get you to the island")
        else:
            print("Invalid input.YOU LOOSE")
    else:
        print("You entered an invalid option! YOU LOOSE!")

else:
    print("Ooops! Too bad")