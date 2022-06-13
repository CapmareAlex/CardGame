import random
import CardClass as dk
import SimularePLayClassDezvoltata
import EndGameScreen


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

    def checkGame(self,handsChosen, playerCards, botCards):
        valueOfCard , nr = handsChosen[-1]

        freqVal = 0
        for x in playerCards:
            if x.valoare == valueOfCard:
                freqVal += 1
        for x in botCards:
            if x.valoare == valueOfCard:
                freqVal +=1

        return freqVal < nr

    def playGame(self):
        turn = 0
        while True:
            print(f"Player: {self.player.numberOfCards}, PC: {self.bot.numberOfCards}")
            # la inceput trebuie sa am tot pachetul
            deck = dk.Deck()
            if self.player.numberOfCards == 6:
                # trebuie creata o functie final
                print("Bot wins!")
                return EndGameScreen.endGame(False)

            elif self.bot.numberOfCards == 6:
                print("Player wins!")
                return EndGameScreen.endGame(True)
            else:
                deck.shuffle()
                # au fost impartite cartile
                self.player.cards = [deck.drawCard() for i in range(self.player.numberOfCards)]
                self.bot.cards = [deck.drawCard() for i in range(self.bot.numberOfCards)]

                while True:
                    if turn == 0:
                        x=self.player.chooseOption()
                        self.handsChosen.append(x)
                        turn=turn+1
                        if self.bot.youLied(self.mode):
                            turn = 0
                            if self.checkGame(self.handsChosen, self.player.cards, self.bot.cards):
                                print("Castigator e calculator")
                                self.player.numberOfCards += 1
                                break
                            else:
                                print("Tu ai castigat")
                                self.bot.numberOfCards += 1
                                break
                    else:
                        self.handsChosen.append(self.bot.chooseOption(self.handsChosen, self.mode))
                        turn=(turn+1)%2


# tip = 0 - player, tip = 1 - bot
# Player: lista de carti, functie de alegere(selecteaza)
# Bot: list de carti, functie de alegere(calculeaza alegerea)

class Player:
    def __init__(self, tip):
        self.type = tip
        self.cards = []
        self.numberOfCards = 1

    def youLied(self, mode):
        if mode == 'Easy':
            return 1
        else:
            return 0

    def chooseOption(self, handChosen = [], mode = 'Easy'):
        if self.type == 0:
           return SimularePLayClassDezvoltata.play_option(self.cards)



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