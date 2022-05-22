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
list_of_players = []

darts_shot = 0
player_counter = 1
start_score = -301
klar = False

for player in players:
    print(f"\nPlayer: {player_counter} will now play!")
    while not klar:
        input(f"\ntype anything to throw your {darts_shot+1}. dart: ")
        darts_shot += 1

        def give_random_number1(range_start, range_stop):
            random_number = random.randrange(range_start, range_stop)
            return random_number

        one_hit_score1 = give_random_number1(1, 24)
        print(one_hit_score1)
        if one_hit_score1 in range(2, 22):
            def give_random_number2(range_start, range_stop):
                random_number = random.randrange(range_start, range_stop)
                return random_number

            multiplier = give_random_number2(1, 4)
            print(f"multiplier: {multiplier}")

            if multiplier == 2:
                score_from_first_double = ((one_hit_score1-1) * 2)
                score_after_multi = (one_hit_score1 * 2)
                list_of_scores.append(score_after_multi)
                print(f"score: {score_after_multi}")
                klar = True
            elif multiplier in (1, 3):
                print("You must hit a Double multiplier on the first hit")

        else:
            print("You must hit a Double multiplier on the first hit")


    while klar:
        input(f"\ntype anything to throw your {darts_shot+1}. dart: ")
        print()
        darts_shot += 1

        def give_random_number1(range_start, range_stop):
            random_number = random.randrange(range_start, range_stop)
            return random_number


        one_hit_score1 = give_random_number1(1, 24)
        if one_hit_score1 == 1:
            print("hit: 0")
            print(f"Your total score is: {sum(list_of_scores) + (start_score)}")

        elif one_hit_score1 in range(2, 22):
            print(f"hit: {one_hit_score1-1}")

            def give_random_number2(range_start, range_stop):
                random_number = random.randrange(range_start, range_stop)
                return random_number


            multiplier = give_random_number2(1, 4)
            print(f"multiplier: {multiplier}")

            if multiplier == 2:
                score_after_multi = ((one_hit_score1-1) * 2)
                list_of_scores.append(score_after_multi)
                print(f"score: {score_after_multi}")
                print(f"Your total score is: {sum(list_of_scores) + (start_score)}")

            elif multiplier == 3:
                score_after_multi = ((one_hit_score1-1) * 3)
                list_of_scores.append(score_after_multi)
                print(f"score: {score_after_multi}")
                print(f"Your total score is: {sum(list_of_scores) + (start_score)}")

            elif multiplier == 1:
                list_of_scores.append(one_hit_score1-1)
                print(f"score: {one_hit_score1-1}")
                print(f"Your total score is: {sum(list_of_scores) + (start_score)}")

        elif one_hit_score1 == 22:
            score_to_scoreboard = 25
            list_of_scores.append(score_to_scoreboard)
            print(f"OUTER BULLSEYE!\nscore: {score_to_scoreboard}")
            print(f"Your total score is: {sum(list_of_scores) + (start_score)}")

        elif one_hit_score1 == 23:
            score_to_scoreboard = 50
            list_of_scores.append(score_to_scoreboard)
            print(f"BULLSEYE!\nscore: {score_to_scoreboard}")
            print(f"Your total score is: {sum(list_of_scores) + (start_score)}")

        if sum(list_of_scores) + (start_score) >= 0:
            if sum(list_of_scores) + (start_score) == 0 and multiplier == 2:
                list_of_players.append(f"Player{player_counter}")
                final_score.append(f"=={darts_shot}==")
                list_of_scores.clear()
                darts_shot = 0
                player_counter += 1
                klar = False
            else:
                print(f"You have to land on exactly 0, try again!")
                list_of_scores.pop()
                print(f"your actual score is {sum(list_of_scores) + (start_score)}")
                if sum(list_of_scores) + (start_score) in (-1, -3, -5):
                    list_of_scores.pop()



print()
print(f"=======SCOREBOARD=======")
print(list_of_players)
print(f"{final_score} darts thrown")