import random

print ("Welcome to RSP")
choice= input ("Do you want to play? ").lower()

if choice != "yes":
    quit()
else:
    print("Let's Play")

option=["rock","paper","scissors"]


user_wins=0
computer_wins=0
draws=0

while True:
    user_choice=input("Enter rock,paper,scissors or q to quit: ").lower()
    if user_choice=="q":
        print ("Computer won: " + str(computer_wins) + " times." )
        print ("Your won: " + str(user_wins) + " times.")
        print("GoodBye!")
        break

    if user_choice not in ["rock","paper","scissors"]:
        continue

    random_number=random.randint(0,2)

    #rock is 0,scissors is 1,paper is 2.
    computer_choice=option[random_number]
    print("Computer says: " + computer_choice)

    if computer_choice==option[0] and user_choice==option[1]:
        user_wins=user_wins+1
    elif computer_choice==option[1] and user_choice==option[0]:
        computer_wins=computer_wins+1
    elif computer_choice==option[1] and user_choice==option[2]:
        user_wins=user_wins+1
    elif computer_choice==option[2] and user_choice==option[1]:
        computer_wins=computer_wins+1
    elif computer_choice==option[0] and user_choice==option[2]:
        computer_wins=computer_wins+1
    elif computer_choice==option[2] and user_choice==option[0]:
        user_wins=user_wins+1
    else:
        draws=draws+1
        continue
        

print ("Computer won: " + str(computer_wins) + " times." )
print ("Your won: " + str(user_wins) + " times.")
print ("Draws: " + str(draws))
print("GoodBye!")
    
        
