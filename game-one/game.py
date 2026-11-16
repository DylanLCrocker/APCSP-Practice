import random
# 0 = Rock
# 1 = Paper
# 2 = Scissors

def stratagy_random_move() :
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
    return winner_statement, result

def count_wins(player_1_throw, player_2_throw) :
    if (player_1_throw == player_2_throw) :
        ties += 1
    elif (player_1_throw == "Rock" and player_2_throw == "Scissors") :
        p1_wins += 1
    elif (player_1_throw == "Paper" and player_2_throw == "Rock"):
        p1_wins += 1
    elif (player_1_throw == "Scissors" and player_2_throw == "Paper"):
        p1_wins += 1
    else:
        p2_wins += 1
    return "(" + str(p1_wins), str(p2_wins), str(ties) +")"

def main():
    print("0 = Rock, 1 = Paper, 2 = Scissors")
    for i in range(1, 6, 1) :
        print("Round: " + str(i))
        player_1_throw = int(input("Player 1 Move: "))
        player_2_throw = int(stratagy_random_move())

        player_1_throw = convert_move_to_string(player_1_throw)
        player_2_throw = convert_move_to_string(player_2_throw)  

        winner_statement, result = find_winner(player_1_throw, player_2_throw) 

        record = count_wins(player_1_throw, player_2_throw)
        print(winner_statement)
        print(result)
    print(count_wins(player_1_throw, player_2_throw))

if __name__ == "__main__":
    main()