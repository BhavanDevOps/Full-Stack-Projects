player_1=input()
player_2=input()



if player_1 == player_2:
    print("Tie")
elif player_1 == "Rock":
    if player_2 == "Paper":
        print("Anjali Wins")
    else:
        print("Abhinav Wins")
elif player_1 == "Scissors":
    if player_2 == "Rock":
        print("Anjali Wins")
    else:
        print("Abhinav Wins")
elif player_1 == "Scissors":
    if player_2 == "Paper":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
