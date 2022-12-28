import random

print("Welcome to Guess a number!")
choice=input ("Do you want to play? ")
print(choice)
if choice.lower()=="yes":
    print("Let's start:) ")

top= input("What is your range of numbers: ")
top=int(top)

if top<=0:
    print("Enter a number larger than zero.")
    top= input("What is your range of numbers: ")
    top=int(top)

else:
    random_number=random.randint(0,top)


guesses=0

while True:
    guesses=guesses+1
    user_guess=input("Guess a number: ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("Please enter a number again: ")
        continue

    if user_guess==random_number:
        print("You got it")
        break
    if user_guess>random_number:
        print("You were above the number")
    else:
        print("You were below the number")
        

print("You got it in " + str(guesses) + " guesses")
