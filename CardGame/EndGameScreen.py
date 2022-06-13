import pygame
from button import button
import ptext

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
FONT = 'Assets\Fonts\Pixeltype.ttf'
scrInfo = pygame.display.Info()

winSound = pygame.mixer.Sound('Assets/Sounds/winSound.wav')
loseSound = pygame.mixer.Sound('Assets/Sounds/loseSound.mp3')
buttonClickSound = pygame.mixer.Sound('Assets/Sounds/buttonClickSound.wav')

buttonClickSound.set_volume(0.1)
winSound.set_volume(0.1)
loseSound.set_volume(0.1)

def endGame(endResult):
    if endResult:
        winSound.play()
        bg = pygame.image.load("Assets/Images/winTempPic.jpg")
        msg = "YOU \n" \
              "WON"
        clr = 'black'
        pos = (250, 250)
        txt_size = 500
        playAgainButtonPos = (350, 1000)
        mainMenuButtonPos = (700, 1000)
    else:
        loseSound.play()
        bg = pygame.image.load("Assets/Images/loseTempPic.jpg")
        msg = "YOU LOST"
        clr = 'white'
        pos = (575, 700)
        txt_size = 300
        playAgainButtonPos = (700, 1000)
        mainMenuButtonPos = (1260, 1000)

    bg = pygame.transform.scale(bg, (scrInfo.current_w, scrInfo.current_h))
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.blit(bg, (0, 0))

        playAgainButton = button(position= playAgainButtonPos, clr='white', cngclr='#ffcc99', size=(200, 50), text='PLAY AGAIN', font="Assets\Fonts\Pixeltype.ttf", font_size=30)
        mainMenuButton = button(position= mainMenuButtonPos, clr='white', cngclr='#ffcc99', size=(200, 50), text='MAIN MENU', font="Assets\Fonts\Pixeltype.ttf", font_size=30)

        playAgainButton.draw(screen)
        mainMenuButton.draw(screen)

        if playAgainButton.mouseover():
            if pygame.mouse.get_pressed()[0]:
                buttonClickSound.play()
                done = True
                return True

        if mainMenuButton.mouseover():
            if pygame.mouse.get_pressed()[0]:
                buttonClickSound.play()
                pygame.display.update()
                done = True

        clock = pygame.time.Clock()
        ptext.draw(msg, pos, color=clr, fontsize=txt_size, fontname=FONT)
        pygame.display.flip()
        clock.tick(60)

    PHOTO = pygame.image.load("Assets/Images/frameFromGif.jpg")
    PHOTO = pygame.transform.scale(PHOTO, (scrInfo.current_w, scrInfo.current_h))
    screen.blit(PHOTO, (0, 0))
    pygame.display.update()
    return False

