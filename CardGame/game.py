import DisplayBot
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
                print("TEST AICI")
                for x in self.player.cards:
                    print(x.valoare)
                print("_________________________")
                self.bot.cards = [deck.drawCard() for i in range(self.bot.numberOfCards)]

                while True:
                    if turn == 0:
                        x=self.player.chooseOption()
                        self.handsChosen.append(x)
                        turn=turn+1
                        if self.bot.youLied(self.mode):
                            if self.checkGame(self.handsChosen, self.player.cards, self.bot.cards):
                                print("Castigator e calculator. Ai spus o mana care nu exista la masa")
                                self.player.numberOfCards += 1
                                break
                            else:
                                print("Tu ai castigat. Chiar sunt cartile in maini!")
                                self.bot.numberOfCards += 1
                                break
                    else:
                        handBot, option = self.bot.chooseOption(self.handsChosen, self.mode)
                        self.handsChosen.append(handBot)
                        turn=(turn+1)%2
                        if option == 0:
                            if self.checkGame(self.handsChosen, self.player.cards, self.bot.cards):
                                print("Tu ai castigat! Botul a pus o mana care nu exista la masa!")
                                self.bot.numberOfCards += 1
                                break
                            else:
                                print("Caculatorul a castigat! Chiar sunt cartile in maini")
                                self.player.numberOfCards += 1
                                break


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

    def chooseOption(self, handsChosen = [], mode = 'Easy'):
        if self.type == 0:
           return SimularePLayClassDezvoltata.play_option(self.cards)

        else:
            print("TEST")
            return DisplayBot.play(mode, handsChosen, self.cards)