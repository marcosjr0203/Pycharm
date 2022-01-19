import random
print("♢♣♤♥ Welcome to the BlackJack ♢♣♤♥!!!\n")
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",  # ♣
         "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",  # ♥
         "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",  # ♤
         "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]  # ♢
comp = []
user = []
user_score = []
comp_score = []
game_over = False


def is_blackjack(player_score):
    if sum(player_score) == 21:
        return True


def hand(player, player_score):
    card = random.choice(cards)
    if card == "A" and sum(player_score) <= 10:
        player += ["A"]
        player_score += [11]
    elif card == "A" and sum(player_score) > 10:
        player += ["A"]
        player_score += [1]
    elif card == "J":
        player += ["J"]
        player_score += [10]
    elif card == "Q":
        player += ["Q"]
        player_score += [10]
    elif card == "K":
        player += ["K"]
        player_score += [10]
    else:
        player += [card]
        player_score += [card]
    cards.remove(card)
    return player, player_score


hand(user, user_score)
hand(user, user_score)
print(f"Your cards: {user}, Your score: {sum(user_score)}")
if is_blackjack(user_score):
    print("BlackJack!")
    game_over = True
hand(comp, comp_score)
print(f"Computer cards: {comp}, Computer score: {sum(comp_score)}")
if is_blackjack(comp_score):
    print("BlackJack!")
    game_over = True

# Próximos passos:
# 1 - Perguntar ao user se continua ou não - OK
# 2 - Dar mais cartas ao usuário até 21 ou próximo disso - OK
# 3 - Se os pontos do computador forem < 17, mais cartas até >= 17 - OK
# 4 - Transformar 11 em 'A' valendo 1, exceto se a soma das cartas forem <= 10
# - Inserir JQK valendo "10"
# 5 - Tirar as cartas do baralho
# 6 - Extra: Inserir símbolos no lugar dos valores (AJQK)
# 7 - Extra: Sistema de aposta (dobro ou nada)
# 8 - IMPORTANTE: VALIDAÇÃO DE TUDO

while not game_over:
    if is_blackjack(user_score):
        print("Blackjack!")
        game_over = True
    if is_blackjack(comp_score):
        game_over = True
    if input("Do you want another card? [y/n]: ").lower() == "y":
        hand(user, user_score)
        print(f"Your cards: {user}, Your score: {sum(user_score)}")
        if is_blackjack(user_score):
            game_over = True
        if sum(user_score) > 21:
            print("You lose.")
            game_over = True
    else:
        if len(comp) <= 5:
            while sum(comp_score) < 17:
                hand(comp, comp_score)
                print(f"Computer cards: {comp}, Computer score: {sum(comp_score)}")
                if is_blackjack(comp_score):
                    print("Blackjack!")
                    game_over = True
            if sum(comp_score) > 21 and sum(user_score) < 21:
                print("You win!")
                game_over = True
            elif sum(user_score) < sum(comp_score) <= 21:
                print("You lose.")
                game_over = True
            elif sum(comp_score) == sum(user_score):
                print("Draw")
                game_over = True


