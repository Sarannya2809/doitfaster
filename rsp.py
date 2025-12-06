import random
while True:
    user_action=input("enter a choice (rock, paper,cissors):")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.choice(possible_actions)
    print(f"\nYou choose {user_action}, computer choose {computer_action}. \n")
    if user_action == computer_action:
       print(f"both players selected{user_action}") 
    elif user_action =="rock":
        if computer_action=="scissors":
            print("rock smashes scissors u win gng")
        else:
            print ("u loose")
    elif user_action =="paper":
        if computer_action=="rock":
            print("paper smashes rock u win gng")
        else:
            print ("u loose")
    elif user_action =="scissors":
        if computer_action=="paper":
            print("scosoors smashes paper u win gng")
        else:
            print ("u loose")
    play_again=input("play again? (y/n): ")
    if play_again !="y":
        break

