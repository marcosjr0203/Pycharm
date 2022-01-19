import random
import game_data
import logo
print(logo.logo)


def data_random():
    rn = random.randint(0, len(game_data.data))
    data = [f"{game_data.data[rn-1]['name']}",
            f"{game_data.data[rn-1]['description']}",
            f"{game_data.data[rn-1]['country']}",
            f"{game_data.data[rn-1]['follower_count']}"]
    return data


def game():
    score = 0
    hit = True
    while hit:
        if score == 0:
            display_a = data_random()
            alt_a = display_a[3]
            display_b = data_random()
            alt_b = display_b[3]
        else:
            display_a = display_b
            alt_a = alt_b
            display_b = data_random()
            alt_b = display_b[3]
        if display_a[0] != display_b[0]:
            print(f"\33[32m{'':*^50}\n"
                  f"Name: {display_a[0]}\n"
                  f"Occupation: {display_a[1]}\n"
                  f"Country: {display_a[2]}\n"
                  f"{'':*^50}\33[0;0m")
            print(logo.vs)
            print(f"\33[31m{'':*^50}\n"
                  f"Name: {display_b[0]}\n"
                  f"Occupation: {display_b[1]}\n"
                  f"Country: {display_b[2]}\n"
                  f"{'':*^50}\33[0;0m")
        else:
            while not display_a[0] != display_b[0]:
                print(f"\33[32m{'':*^50}\n"
                      f"Name: {display_a[0]}\n"
                      f"Occupation: {display_a[1]}\n"
                      f"Country: {display_a[2]}\n"
                      f"{'':*^50}\33[0;0m")
                print(logo.vs)
                print(f"\33[31m{'':*^50}\n"
                      f"Name: {display_b[0]}\n"
                      f"Occupation: {display_b[1]}\n"
                      f"Country: {display_b[2]}\n"
                      f"{'':*^50}\33[0;0m")
        if int(alt_a) > int(alt_b):
            winner = display_a[0]
            looser = display_b[0]
            higher = alt_a
            lower = alt_b
        elif int(alt_b) > int(alt_a):
            winner = display_b[0]
            looser = display_a[0]
            higher = alt_b
            lower = alt_a
        guess = input("Pick your choice [A] or [B]: ")
        while guess.upper() not in "AB":
            guess = input("Wrong choice.\n"
                          "Pick your choice [A] or [B]: ")
        if guess.upper() == "A":
            if int(higher) == int(alt_a):
                score += 1
                print(f"\33[{random.randint(40, 49)};1;{random.randint(30, 39)}m{random.choice(game_data.score_messages)}\33[0;0m\n"
                      f"{winner} has {higher} million followers.\n"
                      f"{looser} has {lower} million followers.\n"
                      f"\33[34mYour score is {score}\33[0;0m")
            elif int(higher) > int(alt_a):
                print(f"{logo.loose}\n"
                      f"{winner} has {higher} million followers.\n"
                      f"{looser} has {lower} million followers.\n"
                      f"\33[31mYou scored {score}\33[0;0m")
                hit = False
        elif guess.upper() == "B":
            if int(higher) == int(alt_b):
                score += 1
                print(f"\33[{random.randint(40, 49)};1;{random.randint(30, 39)}m"
                      f"{random.choice(game_data.score_messages).upper()}\33[0;0m\n"
                      f"{winner} has {higher} million followers.\n"
                      f"{looser} has {lower} million followers.\n"
                      f"\33[34mYour score is {score}\33[0;0m")
            elif int(higher) > int(alt_b):
                print(f"{logo.loose}\n"
                      f"{winner} has {higher} million followers.\n"
                      f"{looser} has {lower} million followers.\n"
                      f"\33[31mYou scored {score}\33[0;0m")
                hit = False


game()
