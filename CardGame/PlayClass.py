import pygame
import PlayerClass
import time
import CardClass
import buttons
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

pygame.init()
screen=pygame.display.set_mode((800,600))
background=pygame.image.load('background_play.jpg')
back1=pygame.transform.scale(background,(800,600))
card2_b=pygame.image.load('black\\Clovers_2_black.png')
card2_w=pygame.image.load('white\\Clovers_2_white.png')
card2_w=pygame.transform.scale(card2_w,(50,70))
card2_b=pygame.transform.scale(card2_b,(50,70))

card3_b=pygame.image.load('black\\Clovers_3_black.png')
card3_b=pygame.transform.scale(card3_b,(50,70))
card3_w=pygame.image.load('white\\Clovers_3_white.png')
card3_w=pygame.transform.scale(card3_w,(50,70))

card4_b=pygame.image.load('black\\Clovers_4_black.png')
card4_b=pygame.transform.scale(card4_b,(50,70))
card4_w=pygame.image.load('white\\Clovers_4_white.png')
card4_w=pygame.transform.scale(card4_w,(50,70))


card5_b=pygame.image.load('black\\Clovers_5_black.png')
card5_b=pygame.transform.scale(card5_b,(50,70))
card5_w=pygame.image.load('white\\Clovers_5_white.png')
card5_w=pygame.transform.scale(card5_w,(50,70))

card6_b=pygame.image.load('black\\Clovers_6_black.png')
card6_b=pygame.transform.scale(card6_b,(50,70))
card6_w=pygame.image.load('white\\Clovers_6_white.png')
card6_w=pygame.transform.scale(card6_w,(50,70))


card7_b=pygame.image.load('black\\Clovers_7_black.png')
card7_b=pygame.transform.scale(card7_b,(50,70))
card7_w=pygame.image.load('white\\Clovers_7_white.png')
card7_w=pygame.transform.scale(card7_w,(50,70))


card8_b=pygame.image.load('black\\Clovers_8_black.png')
card8_b=pygame.transform.scale(card8_b,(50,70))
card8_w=pygame.image.load('white\\Clovers_8_white.png')
card8_w=pygame.transform.scale(card8_w,(50,70))

card9_b=pygame.image.load('black\\Clovers_9_black.png')
card9_b=pygame.transform.scale(card9_b,(50,70))
card9_w=pygame.image.load('white\\Clovers_9_white.png')
card9_w=pygame.transform.scale(card9_w,(50,70))

card10_b=pygame.image.load('black\\Clovers_10_black.png')
card10_b=pygame.transform.scale(card10_b,(50,70))
card10_w=pygame.image.load('white\\Clovers_10_white.png')
card10_w=pygame.transform.scale(card10_w,(50,70))

cardJ_b=pygame.image.load('black\\Clovers_Jack_black.png')
cardJ_b=pygame.transform.scale(cardJ_b,(50,70))
cardJ_w=pygame.image.load('white\\Clovers_Jack_white.png')
cardJ_w=pygame.transform.scale(cardJ_w,(50,70))

cardQ_b=pygame.image.load('black\\Clovers_Queen_black.png')
cardQ_b=pygame.transform.scale(cardQ_b,(50,70))
cardQ_w=pygame.image.load('white\\Clovers_Queen_white.png')
cardQ_w=pygame.transform.scale(cardQ_w,(50,70))

cardK_b=pygame.image.load('black\\Clovers_King_black.png')
cardK_b=pygame.transform.scale(cardK_b,(50,70))
cardK_w=pygame.image.load('white\\Clovers_King_white.png')
cardK_w=pygame.transform.scale(cardK_w,(50,70))

cardA_b=pygame.image.load('black\\Clovers_A_black.png')
cardA_b=pygame.transform.scale(cardA_b,(50,70))
cardA_w=pygame.image.load('white\\Clovers_A_white.png')
cardA_w=pygame.transform.scale(cardA_w,(50,70))
card2=card2_b
card3=card3_b
card4=card4_b
card5=card5_b
card6=card6_b
card7=card7_b
card8=card8_b
card9=card9_b
card10=card10_b
cardJ=cardJ_b
cardQ=cardQ_b
cardK=cardK_b
cardA=cardA_b
x=0
y=0
colors=['null','b','b','b','b','b','b','b','b','b','b','b','b','b']
running=True
player=PlayerClass.classPLayer([])
player_number_of_cards=player.numberOfCards
card_deck=CardClass.Deck()

card_deck.shuffle()
listofcards=[]
while player_number_of_cards!=0:
    listofcards.append(card_deck.carti[0])
    card_deck.drawCard()
    player_number_of_cards=player_number_of_cards-1
print_cards=[]

for c in listofcards:
    if c.valoare==2:
        print_cards.append(card2_w)
    if c.valoare == 3:
            print_cards.append(card3_w)
    if c.valoare == 4:
            print_cards.append(card4_w)
    if c.valoare == 5:
            print_cards.append(card5_w)
    if c.valoare==6:
        print_cards.append(card6_w)
    if c.valoare==7:
        print_cards.append(card7_w)
    if c.valoare==8:
        print_cards.append(card8_w)
    if c.valoare==9:
        print_cards.append(card9_w)
    if c.valoare==10:
        print_cards.append(card10_w)
    if c.valoare==11:
        print_cards.append(cardJ_w)
    if c.valoare==12:
        print_cards.append(cardQ_w)
    if c.valoare==13:
        print_cards.append(cardK_w)
    if c.valoare==14:
        print_cards.append(cardA_w)
print(len(print_cards))
list_comenzi=[] # pentru selectarea perechilor in caz ca avem mai multe
x_card_player=20
y_card_player=400

button1 = buttons.button(position=(200, 250), size=(60, 80), clr=(220, 220, 220), cngclr=(255, 0, 0), func=fn1, text='O carte')
button2 = buttons.button((300, 250), (60, 80), (220, 220, 220), (255, 0, 0), fn2, 'Pereche')
button3 = buttons.button((400, 250), (60, 80), (220, 220, 220), (255, 0, 0), fn2, 'Cui')
button4 = buttons.button((500, 250), (60, 80), (220, 220, 220), (255, 0, 0), fn2, 'Careu')
button_list=[button1,button2,button3,button4]
while running:
    clicking=False
    pos = pygame.mouse.get_pos()

    screen.blit(back1,(0,0))
    card_blit(card2,20,100)
    card_blit(card3,80,100)
    card_blit(card4,140, 100)
    card_blit(card5,200, 100)
    card_blit(card6,260, 100)
    card_blit(card7,320, 100)
    card_blit(card8, 380, 100)
    card_blit(card9, 440, 100)
    card_blit(card10, 500, 100)
    card_blit(cardJ, 560, 100)
    card_blit(cardQ, 620, 100)
    card_blit(cardK, 680, 100)
    card_blit(cardA, 740, 100)
    show_player_cards(50, 300)
    for c in print_cards:
        card_blit(c, x_card_player, y_card_player)

    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = pygame.mouse.get_pos()

    if(x>=20 and x<80 and y>=100 and y<=182):
        if colors[1]=='b':
            card2=card2_w
            colors[1]='w'
        else:
            card2=card2_b
            colors[1]='b'
    if (x >= 80 and x < 140 and y>=100 and y<=182):
        if colors[2] == 'b':
            card3 = card3_w
            colors[2] = 'w'
        else:
            card3 = card3_b
            colors[2] = 'b'
    if (x >= 140 and x < 200 and y>=100 and y<=182):
        if colors[3] == 'b':
            card4 = card4_w
            colors[3] = 'w'
        else:
            card4 = card4_b
            colors[3] = 'b'
    if (x >= 200 and x < 260 and y>=100 and y<=182):
        if colors[4] == 'b':
            card5 = card5_w
            colors[4] = 'w'
        else:
            card5 = card5_b
            colors[4] = 'b'

    if (x >= 260 and x < 320 and y>=100 and y<=182):
        if colors[5] == 'b':
            card6 = card6_w
            colors[5] = 'w'
        else:
            card6 = card6_b
            colors[5] = 'b'
    if (x >= 320 and x < 380 and y>=100 and y<=182):
        if colors[6] == 'b':
            card7 = card7_w
            colors[6] = 'w'
        else:
            card7 = card7_b
            colors[6] = 'b'
    if (x >= 380 and x < 440 and y>=100 and y<=182):
        if colors[7] == 'b':
            card8 = card8_w
            colors[7] = 'w'
        else:
            card8 = card8_b
            colors[7] = 'b'

    if (x >= 440 and x < 500 and y>=100 and y<=182):
        if colors[8] == 'b':
            card9 = card9_w
            colors[8] = 'w'
        else:
            card9 = card9_b
            colors[8] = 'b'

    if (x >= 500 and x < 560 and y>=100 and y<=182):
        if colors[9] == 'b':
            card10 = card10_w
            colors[9] = 'w'
        else:
            card10 = card10_b
            colors[9] = 'b'

    if (x >= 560 and x < 620 and y>=100 and y<=182):
        if colors[10] == 'b':
            cardJ = cardJ_w
            colors[10] = 'w'
        else:
            cardJ = cardJ_b
            colors[10] = 'b'

    if (x >= 620 and x < 680 and y>=100 and y<=182):
        if colors[11] == 'b':
            cardQ = cardQ_w
            colors[11] = 'w'
        else:
            cardQ = cardQ_b
            colors[11] = 'b'

    if (x >= 680 and x < 740 and y>=100 and y<=182):
        if colors[12] == 'b':
            cardK = cardK_w
            colors[12] = 'w'
        else:
            cardK = cardK_b
            colors[12] = 'b'

    if (x >= 740 and y>=100 and y<=182):
        if colors[13] == 'b':
            cardA = cardA_w
            colors[13] = 'w'
        else:
            cardA = cardA_b
            colors[13] = 'b'

    x=0
    y=0
    for b in button_list:
        b.draw(screen)
    pygame.display.update()