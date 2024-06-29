import random 
from art import logo 

def the_number_chooser():
    numbers = list(range(1,100))
    the_number = random.choice(numbers)
    return the_number
    

def number_guess():
    if level == "easy":
        print("You have 10 attempts remaining to guess the number.")
        
    elif level == "hard":
        print("You have 5 attempts remaining to guess the number.")
    
    return level    

def display_results(guess, the_number):
    if guess<the_number :
        print("Too low.")
    elif guess>the_number:
        print("Too high.")
    elif guess== the_number:
        print("You got it! The answer was", the_number  )
         
    

def find(guess, the_number,level):
    if level== 'easy':
        for _ in range(9):
            guess = int(input("Make a guess:"))
            display_results(guess,the_number)
    elif level== 'hard':
        for _ in range(4):
            guess = int(input("Make a guess:"))
            display_results(guess,the_number)
            if guess == the_number:
                return


            
print(logo)
print("Welcome to the Number Guessing Game!""\n""I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

   

number_guess()



rguess = int(input("Enter your initial guess: "))
the_number= the_number_chooser()


display_results(rguess, the_number)
find(rguess,the_number,level)




        



