import random
import os
def guess(a,b,name="player"):
    guess=0
    number_of_tries=0
    b=b+1 if a==b else b
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
        if lines and lines[0].strip().lower() != "name,leaderboard position":
            lines.insert(0, "name,Leaderboard position\n")

        highScore = None
        
        if len(lines) > 1:
            firstLine = lines[1].strip().split(",")
            highScore = int(firstLine[1])

        if highScore is None or n < highScore:
            f = open("scores.csv", "w")
            f.write("name,Leaderboard position\n")
            f.write(f"{name},{n}\n")
            if len(lines) > 1:
                f.writelines(lines[1:])
            f.close()
        else:
            with open("scores.csv", "a") as f:
                f.write(f"{name},{n}\n")

    except FileNotFoundError:
        with open("scores.csv", "x") as f:
            f.write("name,Leaderboard position\n")
            f.write(f"{name},{n}\n")


            
if __name__=="__main__":
    n=input("Enter your name >")
    a=int(input("Enter the starting range >"))
    b=int(input("Enter the end range >"))
    guess(a,b,n)