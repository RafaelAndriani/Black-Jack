class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.money = 100
        self.playing = True

    def receive_cards(self, cartas):
        self.cards.extend(cartas)
        self.show_cards()

    def get_score(self):
        return sum(list(map(lambda dic: list(dic.values())[0], self.cards)))

    def show_cards(self):
        cards_temp = ""
        for n in self.cards:
            cards_temp += " " + str(list(n.keys())[0])
        print(f"As cartas do {self.name} são: {cards_temp}, seu score é {self.get_score()}")

    def get_cards_values(self):
        return list(map(lambda dic: list(dic.values())[0], self.cards))
