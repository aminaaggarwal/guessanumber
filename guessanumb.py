# import random function to generate a random number

import random

#Ask for the name of the person

print ("Hello! What is your name?")

name = input()

print ( "Well, " + name + ", I am thinking of a number between 1 and 20 ." )

# call the randint function to generate a number between 0 and 20

numb = random. randint(0,20)


# The person needs can only make 6 guesses
 
for guesstaken in range (1,6):
    print("Take a guess")
    guess = int(input())

    if guess > numb :
     print("Your guess is too high")

    elif guess < numb :
        print("Your guess is too high")

    else :
         break

if guess == numb :
 print ("Good Job ,"  + name + "! You guessed my number in " + str(guesstaken) + "guesses!")

else:
 print ("Nope. The number is was thinking was" + numb )
 
      
