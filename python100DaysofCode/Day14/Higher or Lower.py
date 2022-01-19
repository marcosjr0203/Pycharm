import random
import logo
import game_data
print(logo.logo)
print("Try to guess who has more followers on Instagram:")
# random
x = 1
game_over = False

# ACHAR UM MEIO DE SORTEAR SEM REPETIÇÃO UM VALOR PARA "a" E OUTRO PARA "b"
# "a" E "b" NÃO PODEM SER IGUAIS
# TENTAR VALIDAÇÃO
a = 0
b = 0
c = 0

# while there's a correct answer
while not game_over:
    # for not showing a single alternative twice
    while a == b:
        a = random.randint(0, len(game_data.data)-1)
        b = random.randint(0, len(game_data.data)-1)
        c = random.randint(0, len(game_data.data)-1)
        while a == c or b == c:
            c = random.randint(0, len(game_data.data)-1)

    print(f"\n\nROUND {x}: {game_data.data[a]['name'].upper()} x {game_data.data[b]['name'].upper()}")
    print("----------------------------------------")
    print(f"[A]\n{game_data.data[a]['name']}\n"
          f"{game_data.data[a]['description']}\n"
          f"{game_data.data[a]['country']}")
    print(logo.vs)
    print(f"[B]\n{game_data.data[b]['name']}\n"
          f"{game_data.data[b]['description']}\n"
          f"{game_data.data[b]['country']}")
    x += 1
    # correspondig the answer to the letters "a" and "b"
    if game_data.data[a]['follower_count'] > game_data.data[b]['follower_count']:
        winner = game_data.data[a]['name']
        winopt = "a"
    elif game_data.data[b]['follower_count'] > game_data.data[a]['follower_count']:
        winner = game_data.data[b]['name']
        winopt = "b"

    # asking the user
    answer = input(f"\n¨¨¨¨¨¨¨¨ NOW ANSWER: ¨¨¨¨¨¨¨¨\n"
                   f"\nWho has more followers: [A] or [B]?"
                   f"\nType your answer: ").upper()
    # validation
    while answer.upper() != "A" and answer.upper() != "B":
        answer = input("Error! Type only [A] or [B]: ").upper()

    # checking answers
    if answer.upper() == "A" or answer.upper() == "B":
        if answer == winopt.upper():
            a = b
            b = c
        elif answer != winopt.upper():
            print(logo.lose)
            game_over = True

