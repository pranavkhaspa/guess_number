import random
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
        
            
            
         
        
        
if __name__=="__main__":

    a=int(input("Enter the starting range >"))
    b=int(input("Enter the end range >"))
    guess(a,b)