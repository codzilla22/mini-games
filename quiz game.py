print ("Welcome to the Central Quiz!")

choice= input ("Do you want to play? ")
print (choice)

if choice.lower()!="yes":
    quit()
else:
    print ("Okay then! Let's play! :) ")
    score=str(0)
    print("Current score: " + score)

answer = input ("What is 7+15? ")
if answer== "22":
    print("Correct")
    score=int(score)
    score +=1
    score= str(score)
    print("Current score: " + score)
else:
    print ("Incorrect")
    score=score
    print(score)


answer = input ("What is 26 times 3? ")
if answer== "78":
    print("Correct")
    score=int(score)
    score+=1
    score= str(score)
    print("Current score: " + score)
else:
    print ("Incorrect")
    score=score
    print(score)


answer = input ("What is 715/45? ")
if answer== "16":
    print("Correct")
    score=int(score)
    score +=1
    score= str(score)
    print("Current score: " + score)
else:
    print ("Incorrect")
    score=score
    print(score)

print ("Final score is: " + score)
