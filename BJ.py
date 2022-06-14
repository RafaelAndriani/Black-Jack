from Dealer import *

players = []


def check_ace(ace, cards):
    if sum(ace) > 21:
        for index, value in enumerate(ace):
            if value == 11:
                print("11 switched for 1")
                ace[index] = 1
                for i in range(0, len(cards)):
                    cl = cards[i]
                    print(cl)
                    if "As" in cl:
                        cards[i]["As"] = 1
    return sum(ace)


def is_player_playing():
    for p in players:
        if p.jogando:
            return True
    return False


def check_who_lose():
    for p in players:
        if p.playing:
            if p.get_score() < dealer.get_score():
                p.playing = False


def score_board():
    for p in players:
        if p.get_score() > 21:
            print(f"{p.name} your score is {p.get_score()}, YOU LOSE")
        elif p.get_score() < 21 and dealer.get_score() > 21:
            print(f"{p.name} your score is {p.get_score()}, YOU LOSE")
        elif p.get_score() > dealer.get_score():
            print(f"{p.name} your score is {p.get_score()} congratulations, YOU WIN")
        elif p.get_score() == dealer.get_score():
            print(f"{p.name} your score is {p.get_score()}, YOU DRAW")
        elif p.get_score() < dealer.get_score():
            print(f"{p.name} your score is {p.get_score()}, YOU LOSE")


dealer = Dealer()


def start():
    quantity_of_players = int(input("How many players will play?"))
    for _ in range(quantity_of_players):
        players.append(Player(input("Whats you name?")))
    dealer.receive_cards(dealer.give_cards(1))
    for p in players:
        p.receive_cards(dealer.give_cards(2))
    for p in players:
        while p.get_score() < 21 and input(f"{p.name}, do you want buy a card? 'Y' or 'N'? ") == 'y':
            p.receive_cards(dealer.give_cards(1))
            cards_sum = check_ace(p.get_cards_values(), p.cards)
            if cards_sum > 21:
                print(f"{p.name} your score is {p.get_score()} and you lose")
                p.playing = False
    while dealer.get_score() < 16 and is_player_playing:
        dealer.receive_cards(dealer.give_cards(1))
        check_who_lose()


start()
score_board()
