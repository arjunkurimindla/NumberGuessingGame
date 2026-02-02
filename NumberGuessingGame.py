def playagain():
    import random
    num=random.randint(1,100)
    return num
count=1
guess=0
nu=playagain()
while nu!=guess:
    try:
        guess = int(input("guess the number :"))
        if guess<nu:
            print(f"Guessed number {guess} is low!! enter greater number")
            count+=1
        elif guess>nu:
            print(f"Guessed number {guess} is high!! enter lesser number")
            count+=1
        else:
            print(f"Guessed number {guess} matches with number {nu} in {count} attempts")
            play=input("want to play again {y/n}").lower()
            nu = playagain()
            count=1
            if play!="y":
                break

    except ValueError:
        print("enter valid input")

