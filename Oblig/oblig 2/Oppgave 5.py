import random

print("======Tarjeis Dart Spill======")
print()

amount_of_players = int(input(f"How many players will play the game?: "))

list_of_players = []
list_of_scores = []

player_counter = 1
close = False
while not close:
    print(f"player {player_counter} will go now!")

    input(f"type anything to throw your first dart: ")
    def give_random_number1(range_start, range_stop):
        random_number = random.randrange(range_start, range_stop)
        return random_number

    one_hit_score1 = give_random_number1(1, 61)
    print(one_hit_score1)

    input(f"type anything to throw your second dart: ")
    def give_random_number2(range_start, range_stop):
        random_number = random.randrange(range_start, range_stop)
        return random_number
    one_hit_score2 = give_random_number2(1, 61)
    print(one_hit_score2)

    input(f"type anything to throw your last dart: ")
    def give_random_number3(range_start, range_stop):
        random_number = random.randrange(range_start, range_stop)
        return random_number
    one_hit_score3 = give_random_number3(1, 61)
    print(one_hit_score3)

    print()
    score = one_hit_score1 + one_hit_score2 + one_hit_score3
    print(f"Your final score is {score}")
    print()
    player_counter += 1
    list_of_players.append(f"Player {player_counter-1}")
    list_of_scores.append(f"==={score}===")

    if player_counter > amount_of_players:
        break

print(f"=======SCOREBOARD=======")
print(list_of_players)
print(list_of_scores)



