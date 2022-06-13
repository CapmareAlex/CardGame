import pygame
import PlayerClass
import time
import CardClass
import button
import buttons
import game
import ptext
def card_blit(card,x,y):
    screen.blit(card,(x,y))

def show_player_cards(x,y):
     font = pygame.font.Font('freesansbold.ttf', 32)
     player_show=font.render("Player Cards: ", True,(255,255,255))
     #player_show=pygame.transform.scale(player_show,(50,80))
     screen.blit(player_show,(x,y))


def fn1():
    print('O carte')
def fn2():
    print('Pereche')
def fn3():
    print('Cui')
def fn4():
    print('Careu')
def fn5():
    print('Submit')
def play_option():
    global screen,scrInfo,background,back1


    card2_b = pygame.image.load('Assets\\cards\\black\\2_inima.png')
    card2_w = pygame.image.load('Assets\\cards\\white\\2_inima.png')
    card2_w = pygame.transform.scale(card2_w, (70, 90))
    card2_b = pygame.transform.scale(card2_b, (70, 90))

    card3_b = pygame.image.load('Assets\\cards\\black\\3_inima.png')
    card3_b = pygame.transform.scale(card3_b, (70, 90))
    card3_w = pygame.image.load('Assets\\cards\\white\\3_inima.png')
    card3_w = pygame.transform.scale(card3_w, (70, 90))

    card4_b = pygame.image.load('Assets\\cards\\black\\4_inima.png')
    card4_b = pygame.transform.scale(card4_b, (70, 90))
    card4_w = pygame.image.load('Assets\\cards\\white\\4_inima.png')
    card4_w = pygame.transform.scale(card4_w, (70, 90))

    card5_b = pygame.image.load('Assets\\cards\\black\\5_inima.png')
    card5_b = pygame.transform.scale(card5_b, (70, 90))
    card5_w = pygame.image.load('Assets\\cards\\white\\5_inima.png')
    card5_w = pygame.transform.scale(card5_w, (70, 90))

    card6_b = pygame.image.load('Assets\\cards\\black\\6_inima.png')
    card6_b = pygame.transform.scale(card6_b, (70, 90))
    card6_w = pygame.image.load('Assets\\cards\\white\\6_inima.png')
    card6_w = pygame.transform.scale(card6_w, (70, 90))

    card7_b = pygame.image.load('Assets\\cards\\black\\7_inima.png')
    card7_b = pygame.transform.scale(card7_b, (70, 90))
    card7_w = pygame.image.load('Assets\\cards\\white\\7_inima.png')
    card7_w = pygame.transform.scale(card7_w, (70, 90))

    card8_b = pygame.image.load('Assets\\cards\\black\\8_inima.png')
    card8_b = pygame.transform.scale(card8_b, (70, 90))
    card8_w = pygame.image.load('Assets\\cards\\white\\8_inima.png')
    card8_w = pygame.transform.scale(card8_w, (70, 90))

    card9_b = pygame.image.load('Assets\\cards\\black\\9_inima.png')
    card9_b = pygame.transform.scale(card9_b, (70, 90))
    card9_w = pygame.image.load('Assets\\cards\\white\\9_inima.png')
    card9_w = pygame.transform.scale(card9_w, (70, 90))

    card10_b = pygame.image.load('Assets\\cards\\black\\10_inima.png')
    card10_b = pygame.transform.scale(card10_b, (70, 90))
    card10_w = pygame.image.load('Assets\\cards\\white\\10_inima.png')
    card10_w = pygame.transform.scale(card10_w, (70, 90))

    cardJ_b = pygame.image.load('Assets\\cards\\black\\11_inima.png')
    cardJ_b = pygame.transform.scale(cardJ_b, (70, 90))
    cardJ_w = pygame.image.load('Assets\\cards\\white\\11_inima.png')
    cardJ_w = pygame.transform.scale(cardJ_w, (70, 90))

    cardQ_b = pygame.image.load('Assets\\cards\\black\\12_inima.png')
    cardQ_b = pygame.transform.scale(cardQ_b, (70, 90))
    cardQ_w = pygame.image.load('Assets\\cards\\white\\12_inima.png')
    cardQ_w = pygame.transform.scale(cardQ_w, (70, 90))

    cardK_b = pygame.image.load('Assets\\cards\\black\\13_inima.png')
    cardK_b = pygame.transform.scale(cardK_b, (70, 90))
    cardK_w = pygame.image.load('Assets\\cards\\white\\13_inima.png')
    cardK_w = pygame.transform.scale(cardK_w, (70, 90))

    cardA_b = pygame.image.load('Assets\\cards\\black\\14_inima.png')
    cardA_b = pygame.transform.scale(cardA_b, (70, 90))
    cardA_w = pygame.image.load('Assets\\cards\\white\\14_inima.png')
    cardA_w = pygame.transform.scale(cardA_w, (70, 90))
    card2 = card2_b
    card3 = card3_b
    card4 = card4_b
    card5 = card5_b
    card6 = card6_b
    card7 = card7_b
    card8 = card8_b
    card9 = card9_b
    card10 = card10_b
    cardJ = cardJ_b
    cardQ = cardQ_b
    cardK = cardK_b
    cardA = cardA_b
    x = 0
    y = 0
    colors = ['null', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    running = True
    player = PlayerClass.classPLayer([])
    player_number_of_cards = player.numberOfCards
    card_deck = CardClass.Deck()

    card_deck.shuffle()
    listofcards = []
    while player_number_of_cards != 0:
        listofcards.append(card_deck.carti[0])
        card_deck.drawCard()
        player_number_of_cards = player_number_of_cards - 1
    print_cards = []

    for c in listofcards:
        if c.valoare == 2:
            print_cards.append(card2_w)
        if c.valoare == 3:
            print_cards.append(card3_w)
        if c.valoare == 4:
            print_cards.append(card4_w)
        if c.valoare == 5:
            print_cards.append(card5_w)
        if c.valoare == 6:
            print_cards.append(card6_w)
        if c.valoare == 7:
            print_cards.append(card7_w)
        if c.valoare == 8:
            print_cards.append(card8_w)
        if c.valoare == 9:
            print_cards.append(card9_w)
        if c.valoare == 10:
            print_cards.append(card10_w)
        if c.valoare == 11:
            print_cards.append(cardJ_w)
        if c.valoare == 12:
            print_cards.append(cardQ_w)
        if c.valoare == 13:
            print_cards.append(cardK_w)
        if c.valoare == 14:
            print_cards.append(cardA_w)
    # print(len(print_cards))
    list_comenzi = []  # pentru selectarea perechilor in caz ca avem mai multe
    x_card_player = 20
    y_card_player = 400

    button1 = buttons.button(position=(200, 250), size=(50, 70), clr=(220, 220, 220), cngclr=(255, 0, 0), func=fn1,
                            text='O carte')
    button2 = buttons.button((300, 250), (50, 70), (220, 220, 220), (255, 0, 0), fn2, 'Pereche')
    button3 = buttons.button((400, 250), (50, 70), (220, 220, 220), (255, 0, 0), fn3, 'Cui')
    button4 = buttons.button((500, 250), (50, 70), (220, 220, 220), (255, 0, 0), fn4, 'Careu')
    submitButton = button.button(position=(1070, 600), clr='white',
                        cngclr='#ffcc99', size=(200, 50), text='Submit', font='Assets\Fonts\Pixeltype.ttf', font_size=30)
    button_list = [button1, button2, button3, button4, submitButton]
    button_x = 0
    button_y = 0
    card_select = 0
    com = 0
    while running:
        clicking = False
        pos = pygame.mouse.get_pos()
        list_of_submit = []
        x_submit = 400
        y_submit = 500
        screen.blit(back1, (0, 0))
        card_blit(card2, 20, 100)
        card_blit(card3, 100, 100)
        card_blit(card4, 180, 100)
        card_blit(card5, 260, 100)
        card_blit(card6, 340, 100)
        card_blit(card7, 420, 100)
        card_blit(card8, 500, 100)
        card_blit(card9, 580, 100)
        card_blit(card10, 660, 100)
        card_blit(cardJ, 740, 100)
        card_blit(cardQ, 820, 100)
        card_blit(cardK, 900, 100)
        card_blit(cardA, 980, 100)
        show_player_cards(50, 300)
        for c in print_cards:
            card_blit(c, x_card_player, y_card_player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        nr_culori = 0
        for x_c in colors:
            if x_c == 'w':
                nr_culori = nr_culori + 1
        if (x >= 20 and x < 100 and y >= 100 and y <= 182):
            if colors[1] == 'b' and nr_culori == 0:
                card2 = card2_w
                colors[1] = 'w'
            else:
                card2 = card2_b
                colors[1] = 'b'
        if (x >= 100 and x < 180 and y >= 100 and y <= 182):
            if colors[2] == 'b' and nr_culori == 0:
                card3 = card3_w
                colors[2] = 'w'
            else:
                card3 = card3_b
                colors[2] = 'b'
        if (x >= 180 and x < 260 and y >= 100 and y <= 182):
            if colors[3] == 'b' and nr_culori == 0:
                card4 = card4_w
                colors[3] = 'w'
            else:
                card4 = card4_b
                colors[3] = 'b'
        if (x >= 260 and x < 340 and y >= 100 and y <= 182):
            if colors[4] == 'b' and nr_culori == 0:
                card5 = card5_w
                colors[4] = 'w'
            else:
                card5 = card5_b
                colors[4] = 'b'

        if (x >= 340 and x < 420 and y >= 100 and y <= 182):
            if colors[5] == 'b' and nr_culori == 0:
                card6 = card6_w
                colors[5] = 'w'
            else:
                card6 = card6_b
                colors[5] = 'b'
        if (x >= 420 and x < 500 and y >= 100 and y <= 182):
            if colors[6] == 'b' and nr_culori == 0:
                card7 = card7_w
                colors[6] = 'w'
            else:
                card7 = card7_b
                colors[6] = 'b'
        if (x >= 500 and x < 580 and y >= 100 and y <= 182):
            if colors[7] == 'b' and nr_culori == 0:
                card8 = card8_w
                colors[7] = 'w'
            else:
                card8 = card8_b
                colors[7] = 'b'

        if (x >= 580 and x < 660 and y >= 100 and y <= 182):
            if colors[8] == 'b' and nr_culori == 0:
                card9 = card9_w
                colors[8] = 'w'
            else:
                card9 = card9_b
                colors[8] = 'b'

        if (x >= 660 and x < 740 and y >= 100 and y <= 182):
            if colors[9] == 'b' and nr_culori == 0:
                card10 = card10_w
                colors[9] = 'w'
            else:
                card10 = card10_b
                colors[9] = 'b'

        if (x >= 740 and x < 820 and y >= 100 and y <= 182):
            if colors[10] == 'b' and nr_culori == 0:
                cardJ = cardJ_w
                colors[10] = 'w'
            else:
                cardJ = cardJ_b
                colors[10] = 'b'

        if (x >= 820 and x < 900 and y >= 100 and y <= 182):
            if colors[11] == 'b' and nr_culori == 0:
                cardQ = cardQ_w
                colors[11] = 'w'
            else:
                cardQ = cardQ_b
                colors[11] = 'b'

        if (x >= 900 and x < 980 and y >= 100 and y <= 182):
            if colors[12] == 'b' and nr_culori == 0:
                cardK = cardK_w
                colors[12] = 'w'
            else:
                cardK = cardK_b
                colors[12] = 'b'

        if (x >= 980 and y >= 100 and y <= 182):
            if colors[13] == 'b' and nr_culori == 0:
                cardA = cardA_w
                colors[13] = 'w'
            else:
                cardA = cardA_b
                colors[13] = 'b'
        if (x >= 200 and x < 300 and y >= 220 and y <= 350):
            com = 1
        if (x >= 300 and x < 400 and y >= 220 and y <= 350):
            com = 2
        if (x >= 400 and x < 500 and y >= 220 and y <= 350):
            com = 3
        if (x >= 500 and y >= 220 and y <= 390):
            com = 4
        poz = 0
        nr = 0
        for x in range(0, len(colors)):
            if colors[x] == 'w':
                poz = x
                nr = nr + 1

        if poz == 1:
            card_select = card2_w
        if poz == 2:
            card_select = card3_w
        if poz == 3:
            card_select = card4_w
        if poz == 4:
            card_select = card5_w
        if poz == 5:
            card_select = card6_w
        if poz == 6:
            card_select = card7_w
        if poz == 7:
            card_select = card8_w
        if poz == 8:
            card_select = card9_w
        if poz == 9:
            card_select = card10_w
        if poz == 10:
            card_select = cardJ_w
        if poz == 11:
            card_select = cardQ_w
        if poz == 12:
            card_select = cardK_w
        if poz == 13:
            card_select = cardA_w
        if poz == 0:
            card_select = 0
            com = 0
        if card_select != 0:
            for x1 in range(0, com):
                card_blit(card_select, x_submit, y_submit)
                x_submit = x_submit + 50

            list_of_submit=(poz+1,com)
        if submitButton.mouseover():
            if pygame.mouse.get_pressed()[0]:
                print(list_of_submit)
                #computer receptioneaza tuplul de carti catre computer
                #apoi computerul zice daca am mintit sau nu 
                return list_of_submit


        x = 0
        y = 0

        for b in button_list:
            b.draw(screen)

        pygame.display.update()


pygame.init()
scrInfo = pygame.display.Info()
screen = pygame.display.set_mode((scrInfo.current_w, scrInfo.current_h), pygame.FULLSCREEN, pygame.RESIZABLE)
background = pygame.image.load('background_play.jpg')
back1 = pygame.transform.scale(background, (scrInfo.current_w, scrInfo.current_h))