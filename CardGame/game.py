import random

import deck as dk

class Game:
    def __init__(self, mode):
        # self.deck = Deck()
        self.player = Player(0)
        self.bot = Player(1)
        self.handsChosen = []
        self.mode = mode
        # in mom in care apasam pe submit, carte_aleasa = .. , mana = ..
        # verif_minti(cartea_aleasa, mana, carti_bot, carti_player)
        # in cartile de bot + cartilde de player se gasesc carte* mana, atunci return 1, else return 0

    def playGame(self):
        turn = 0
        while True:
            # la inceput trebuie sa am tot pachetul
            deck = dk.Deck()
            if len(self.player.cards) == 6:
                # trebuie creata o functie final
                print("Bot wins!")
            elif len(self.bot.cards) == 6:
                print("Player wins!")
            else:
                deck.shuffle()
                # au fost impartite cartile
                self.player.cards = [deck.drawCard() for i in range(len(self.player.cards))]
                self.bot.cards = [deck.drawCard() for i in range(len(self.bot.cards))]

                while True:
                    if turn == 0:
                        self.handsChosen.append(self.player.chooseOption())
                    else:
                        self.handsChosen.append(self.bot.chooseOption(self.handsChosen, self.mode))



# tip = 0 - player, tip = 1 - bot
# Player: lista de carti, functie de alegere(selecteaza)
# Bot: list de carti, functie de alegere(calculeaza alegerea)

class Player:
    def __init__(self, tip):
        self.type = tip
        self.cards = []
        # self.numberOfCards = 0

    def chooseOption(self, handChosen = None, mode = 'Easy'):
        if self.type == 0:
            pass
            # codul pentru afisarea ecranului de selectie(tabel, butoane - ce are Giani)


        else:
            if mode == 'Easy':

                valueOfCard, nr = handChosen[-1]

                # retinem un vector de frecventa pentru carti
                freqOfCards = dict()
                for card in self.cards:
                    if card.valoare in freqOfCards:
                        freqOfCards[card.valoare] += 1
                    else:
                        freqOfCards[card.valoare] = 1

                # s-ar putea sa nu mearga
                sortedKeys = sorted(freqOfCards.keys())

                # daca avem o mana mai mare in pachet, o alegem
                for key in sortedKeys:
                    if key == valueOfCard:
                        if freqOfCards[key] > nr:
                            return (key, nr + 1)
                    elif key > valueOfCard:
                        if freqOfCards[key] >= nr:
                            return (key, nr)

                # daca nu avem o mana mai mare, o alegem pe prima
                # mai mare decat cea zisa de jucator
                if valueOfCard < 14:
                    return (valueOfCard + 1, nr)
                else:
                    return (2, nr + 1)

            else :
                valueOfCard, nr = handChosen[-1]
                rdm = random.randint(0,1)   #generam random un nr
                if rdm % 2 == 0:
                    freqOfCards = dict()
                    for card in self.cards:
                        if card.valoare in freqOfCards:
                            freqOfCards[card.valoare] += 1
                        else:
                            freqOfCards[card.valoare] = 1

                    # s-ar putea sa nu mearga
                    sortedKeys = sorted(freqOfCards.keys())

                    for key in sortedKeys:
                        if key == valueOfCard:
                            if freqOfCards[key] > nr:
                                return (key, nr + 1)
                        elif key > valueOfCard:
                            if freqOfCards[key] >= nr:
                                return (key, nr)

                    if valueOfCard < 14:
                        return (valueOfCard + 1, nr)
                    else:
                        return (2, nr + 1)

                else:
                    if valueOfCard < 14:
                        return (valueOfCard + 1, nr)
                    else:
                        return (2, nr + 1)

            # codul pentru alegerea optiunii bot-ului, dupa care o afisez pe ecran
            #     minti(se apeleaza fc)       cotninua(f continua - > alegerea 0)

# self.player = classPLayer()

# Deck = Deck()
# Deck.creare()
# Deck.shuffle()
# #Deck.__str__()
#
# card = Deck.drawCard()
# print(card.__str__())
# print(Deck)
#
# class classPLayer:
#     nrCarti = 6
#     def __init__(self, ListOfCards):
#         self.ListOfCards = ListOfCards
#         self.ok = 0   # ok are rolul de a stii daca jucatorul a mintit sau nu 0 a mintit 1 nu
#         self.numberOfCards = 1
#
#     def cardsAfterShuffle(self, ListOfCards):
#         self.ListOfCards = ListOfCards
#
#     def increaseNumberOfCards(self):
#         if self.ok == 1:
#             self.numberOfCards = self.numbersOfCards + 1
#             self.ok = 0
#
#     def game_over(self):
#         cls = self.__class__
#         if self.numberOfCards == cls.nrCarti:
#             return "You are out"
#         else:
#             return "Continue to play"
#
#     def continue_to_play(self):
#     #variabila tour_of_cards contine mana spusa de jucatorul
#         return 1
#     def said_minti(self, cards_in_total, hands_cards):
#         is_in = 0
#         for card in hands_cards:
#             if card in cards_in_total:
#                 is_in = is_in + 1
#         if is_in == len(hands_cards):
#             return "Minti"
#         else:
#             return "Corect"
#
#
#     def a_mintit(self):
#         self.ok = 1

# c=classPLayer([1,2,4,5])
# c.cardsAfterShuffle([1,2,3,3,34,3,3])
# print(c.ListOfCards)
# print(c.game_over())