import random
import os
def guess(a,b,name="player"):
    guess=0
    number_of_tries=0
    random_number=random.randrange(a,b)
    while(1):
        number_of_tries+=1
        guess=int(input("Guess the number>"))
        if(guess>random_number):
            print("Too high! Try again!")
        elif(guess<random_number):
            print("go higher!Try again!")
        elif(guess==random_number):
            print(f"{name} you guessed it right in {number_of_tries} tries!!")
            break
    score(name,number_of_tries)
def score(name, n):
    try:
        f = open("scores.csv", "r")
        lines = f.readlines()
        f.close()

        highScore = None

        if lines:
            firstLine = lines[0].strip().split(",")
            highScore =  int(firstLine[1])

        if highScore is None or n < highScore:
            f= open("scores.csv", "w") 
            f.write(f"{name},{n}\n")
            f.close()

            if highScore is not None:
                    f.writelines(lines)  
        else:
            f= open("scores.csv", "a")
            f.write(f"{name},{n}\n")
            f.close()

    except FileNotFoundError:
        f= open("scores.csv", "x")
        f.write(f"name,Leaderboard position\n{name},{n}\n")
        f.close()

            
if __name__=="__main__":
    n=input("Enter your name >")
    a=int(input("Enter the starting range >"))
    b=int(input("Enter the end range >"))
    guess(a,b,n)