class classPLayer:
    nrCarti=6
    def __init__(self,ListOfCards):
        self.ListOfCards=ListOfCards
        self.ok=0   # ok are rolul de a stii daca jucatorul a mintit sau nu 0 a mintit 1 nu
        self.numberOfCards=1
    def cardsAfterShuffle(self,ListOfCards):
        self.ListOfCards=ListOfCards
    def increaseNumberOfCards(self):
        if self.ok==1:
            self.numberOfCards=self.numbersOfCards+1
            self.ok=0
    def game_over(self):
        cls = self.__class__
        if self.numberOfCards==cls.nrCarti:
            return "You are out"
        else:
            return "Continue to play"
    def continue_to_play(self):
    #variabila tour_of_cards contine mana spusa de jucatorul
        return 1
    def said_minti(self, cards_in_total,hands_cards):
        is_in=0
        for card in hands_cards:
            if card in cards_in_total:
                is_in=is_in+1
        if is_in==len(hands_cards):
            return "Minti"
        else:
            return "Corect"

    def a_mintit(self):
        self.ok=1
