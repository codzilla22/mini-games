
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data=(line.rstrip())
            user, passw, acc = data.split("|")
            print ("User: " + user )
            print ("Password: " + passw)
            print ("Account: " + acc)

            
def add():
    user_name=input("Account name: ")
    pwd=input("Password: ")
    account= input("Account for: ")
    with open("passwords.txt", "a") as f:
        f.write(user_name + "|" + pwd + "|" + account + "\n")


i=0

while i<3:
        
    passwords=[#save a passsword here]
    master_pwd=input("Input a login password: ")

    if master_pwd not in passwords[0]:
        print ("Invalid input.Try again: ")
        i=i+1

        if i==3:
            print("You are a pirate. ")
            quit()
    else:
        print("Welcome")
        while True:

            choice=input("Would you like to view an existing password or add a new password(Enter view or add)? You can press q to quit: ")

            if choice=="q":
                quit()

            if choice=="view":
                view()
            elif choice=="add":
                add()
            else:
                print ("Invalid input. ")
                continue
