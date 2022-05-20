import random

class Card:

    def __init__(self, valoare, culoare):
        self.valoare = valoare
        self.culoare = culoare

    def __str__(self):
        return str(self.valoare) + " de " + str(self.culoare)

# a = Card(7, "trefla")
# print(a)


class Deck:
    #constructorul clasei
    def __init__(self):
        self.carti = []
        self.creare()

    #metoda prin care adaugam cartile
    def creare(self):
        for cul in ["Trefla", "Inima", "Frunza", "Romb"]:
            for val in range(1, 14):
                self.carti.append(Card(val, cul))

    #metoda de afisare
    def __str__(self):
        for carte in self.carti:
            print(carte)

    #metoda prin care amestecam cartile
    def shuffle(self):
        for i in range(len(self.carti) - 1, 0, -1):
            r = random.randint(0, i)
            self.carti[i], self.carti[r] = self.carti[r], self.carti[i]

    #metoda prin care eliminam din pachet cartea impartita la un jucator
    def drawCard(self):
        return self.carti.pop()

# Deck = Deck()
# Deck.creare()
# Deck.shuffle()
# #Deck.__str__()
#
# card = Deck.drawCard()
# print(card.__str__())
# print(Deck)