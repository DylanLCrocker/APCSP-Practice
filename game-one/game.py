import random
# 0 = Rock
# 1 = Paper
# 2 = Scissors

def random_move() :
    return random.randint(0,2)

def convert_move_to_string(player_num_throw) :
    if player_num_throw  == 0 :
        player_num_throw = "Rock"
    elif player_num_throw  == 1:
        player_num_throw = "Paper"
    else :
        player_num_throw = "Scissors"
    return player_num_throw

def find_winner(player_1_throw, player_2_throw) :
    result = "Und"
    winner_statement = "Und"
    if (player_1_throw == player_2_throw) :
        result = "It's a Tie"
        winner_statement = str(player_1_throw) + " = " + str(player_2_throw)
    elif (player_1_throw == "Rock" and player_2_throw == "Scissors") :
        result = "Player 1 Wins!"
        winner_statement = str(player_1_throw) + " > " + str(player_2_throw)
    elif (player_1_throw == "Paper" and player_2_throw == "Rock"):
        result = "Player 1 Wins!"
        winner_statement = str(player_1_throw) + " > " + str(player_2_throw)
    elif (player_1_throw == "Scissors" and player_2_throw == "Paper"):
        result = "Player 1 Wins!"
        winner_statement = str(player_1_throw) + " > " + str(player_2_throw)
    else:
        result = "Player 2 Wins!"
        winner_statement = str(player_2_throw) + " > " + str(player_1_throw)
    return winner_statement + ", " + result

def main():
    player_1_throw = int(random_move())
    player_2_throw = int(random_move())

    player_1_throw = convert_move_to_string(player_1_throw)
    player_2_throw = convert_move_to_string(player_2_throw)  

    result_and_statement = find_winner(player_1_throw, player_2_throw) 

    print("Player 1 threw : " + player_1_throw)
    print("Player 2 threw : " + player_2_throw)
    print(result_and_statement)


if __name__ == "__main__":
    main()
