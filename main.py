import random
item_list = ["rock","paper","sciccor"]
user = input("enter your move :")
computer_move = random.choice(item_list)
print(f"your move is = {user},computer move is  = {computer_move}")
if user == computer_move:
    print("match is tie")
elif user == "rock":
    if computer_move == "paper":
        print("computer win")
    else:
        print("you win")
elif user == "paper":
    if computer_move == "rock":
        print("you win")
    else:
        print("computer win")
elif user == "sciccor":
    if computer_move == "rock":
        print("you win")  
    else:
        print("computer win")
                                  
    
