import random
print("======Tarjeis Dart Spill======")
print()

amount_of_players = int(input(f"How many players will play the game?: "))
players = []
while amount_of_players >= 1:
    players.append(amount_of_players)
    amount_of_players -= 1

final_score = []
list_of_scores = []
score_from_hit = []
list_of_players = []
darts = int(input(f"How many darts do you want to play with?: "))
darts_shot = 0
player_counter = 1

for player in players:
    print(f"\nThe {player_counter}. player will throw now!")
    while darts >= darts_shot:
        input(f"\ntype anything to throw your {darts_shot+1}. dart: ")
        print()


        def give_random_number1(range_start, range_stop):
            random_number = random.randrange(range_start, range_stop)
            return random_number


        one_hit_score1 = give_random_number1(1, 24)
        if one_hit_score1 == 1:
            print("hit: 0")
            score_from_hit.append(0)

        elif one_hit_score1 in range(2, 21):
            print(f"hit: {one_hit_score1}")


            def give_random_number2(range_start, range_stop):
                random_number = random.randrange(range_start, range_stop)
                return random_number


            multiplier = give_random_number2(1, 4)
            print(f"multiplier: {multiplier}")
            if multiplier == 2:
                score_after_multi = (one_hit_score1 * 2)
                score_from_hit.append(score_after_multi)
                print(f"score: {score_after_multi}")
            elif multiplier == 3:
                score_after_multi = (one_hit_score1 * 3)
                score_from_hit.append(score_after_multi)
                print(f"score: {score_after_multi}")
            elif multiplier == 1:
                score_from_hit.append(one_hit_score1)
                print(f"score: {one_hit_score1}")


        elif one_hit_score1 == 22:
            score_to_scoreboard = 25
            score_from_hit.append(score_to_scoreboard)
            print(f"OUTER BULLSEYE!\nscore: {score_to_scoreboard}")

        elif one_hit_score1 == 23:
            score_to_scoreboard = 50
            score_from_hit.append(score_to_scoreboard)
            print(f"BULLSEYE!\nscore: {score_to_scoreboard}")

        darts_shot += 1
        if darts == darts_shot:
            list_of_players.append(f"Player{player_counter}")
            score_combined = sum(score_from_hit)
            final_score.append(f"=={score_combined}==")
            score_from_hit.clear()
            darts_shot = 0
            player_counter += 1
            break





print()
print(f"=======SCOREBOARD=======")
print(list_of_players)
print(final_score)