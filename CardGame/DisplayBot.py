import random
import pygame

from button import button

def play(mode, handChosen, self_cards):
    global screen, scrInfo
    scrHeight = scrInfo.current_h
    scrWidth = scrInfo.current_w
    buttonsX = scrWidth // 4
    buttonsY = scrHeight // 4
    incrementButtonY = scrHeight // 6
    incrementButtonX = scrWidth // 6
    clock = pygame.time.Clock()
    bot_solution = ()
    hasChosen = False
    pygame.init()
    pygame.display.update()
    done = False
    option = 0
    while not done:

        screen.blit(back1, (0, 0))
        pygame.event.get()
        findSol = False
        if hasChosen == False:
            if mode == 'Easy':

                valueOfCard, nr = handChosen[-1]

                # retinem un vector de frecventa pentru carti
                freqOfCards = dict()
                for card in self_cards:
                    if card.valoare in freqOfCards:
                        freqOfCards[card.valoare] += 1
                    else:
                        freqOfCards[card.valoare] = 1

                # s-ar putea sa nu mearga
                sortedKeys = sorted(freqOfCards.keys())

                # daca avem o mana mai mare in pachet, o alegem
                for key in sortedKeys:
                    if key == valueOfCard:
                        if freqOfCards[key] > nr and findSol == False:
                            findSol = True
                            bot_solution = (key, nr + 1)

                    elif key > valueOfCard and findSol == False:
                        if freqOfCards[key] >= nr:
                            findSol = True
                            bot_solution = (key, nr)


                # daca nu avem o mana mai mare, o alegem pe prima
                # mai mare decat cea zisa de jucator
                if valueOfCard < 14 and findSol == False:
                    findSol = True
                    bot_solution = (valueOfCard + 1, nr)
                elif findSol == False:
                    findSol = True
                    bot_solution = (2, nr + 1)


            else:
                valueOfCard, nr = handChosen[-1]
                rdm = random.randint(0, 1)  # generam random un nr
                if rdm % 2 == 0:
                    freqOfCards = dict()
                    for card in self_cards:
                        if card.valoare in freqOfCards:
                            freqOfCards[card.valoare] += 1
                        else:
                            freqOfCards[card.valoare] = 1

                    # s-ar putea sa nu mearga
                    sortedKeys = sorted(freqOfCards.keys())

                    for key in sortedKeys:
                        if key == valueOfCard:
                            if freqOfCards[key] > nr and findSol == False:
                                findSol = True
                                bot_solution = (key, nr + 1)

                        elif key > valueOfCard and findSol == False:
                            if freqOfCards[key] >= nr:
                                findSol = True
                                bot_solution = (key, nr)

                    if valueOfCard < 14 and findSol == False:
                        findSol = True
                        bot_solution = (valueOfCard + 1, nr)
                    elif findSol == False:
                        findSol = True
                        bot_solution = (2, nr + 1)

                else:
                    if valueOfCard < 14 and bot_solution == False:
                        findSol = True
                        bot_solution = (valueOfCard + 1, nr)
                    elif findSol == False:
                        findSol = True
                        bot_solution = (2, nr + 1)
            hasChosen = True
            print(f"Botul a ales mana{bot_solution}\n")

        liedButton = button(position=(buttonsX, buttonsY + 3 * incrementButtonY), clr='white', cngclr='#ffcc99',
                            size=(200, 50), text='PC LIED', font='Assets\Fonts\Pixeltype.ttf', font_size=30)
        continueButton = button(position=(buttonsX + 3 * incrementButtonX, buttonsY + 3 * incrementButtonY),
                                clr='white', cngclr='#ffcc99', size=(200, 50), text='CONTINUE',
                                font='Assets\Fonts\Pixeltype.ttf', font_size=30)

        liedButton.draw(screen)
        continueButton.draw(screen)
        if liedButton.mouseover():
            if pygame.mouse.get_pressed()[0]:
                option = 0
                done = True
        if continueButton.mouseover():
            if pygame.mouse.get_pressed()[0]:
                option = 1
                done = True
        pygame.display.update()

    return (bot_solution, option)


pygame.init()
scrInfo = pygame.display.Info()
screen = pygame.display.set_mode((scrInfo.current_w, scrInfo.current_h), pygame.FULLSCREEN, pygame.RESIZABLE)
background = pygame.image.load('background_play.jpg')
back1 = pygame.transform.scale(background, (scrInfo.current_w, scrInfo.current_h))
