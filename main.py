import pygame, os
from pygame import *
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption('Горизонтальное меню')
clock = pygame.time.Clock()

img = pygame.image.load('картинка/image.png')
img_rect = img.get_rect()

imgOG = pygame.image.load('картинка/об игре/об игре.png')
imgOG_rect = imgOG.get_rect(topleft=(int(WIDTH // 4), int(HEIGHT // 6)))

font = pygame.font.Font('шрифт/Undertale-Battle-Font.ttf', 35)

menuItems = ['Играть', 'Настройки', 'Об игре', 'Выход']
itemSelected = 0

ob_game = False
drawButtom = False
not_game = False

def draw_ob_game():
    window.blit(imgOG, imgOG_rect)

def draw_buttom():
    text = font.render('Выйти', 0, (255, 255, 255))
    text_rect = text.get_rect(topleft=(int(WIDTH // 2.2), int(HEIGHT // 1.35)))
    window.blit(text, text_rect)

timer = 2

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if not not_game:
                    itemSelected -= 1
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if not not_game:
                    itemSelected += 1
            elif event.key == pygame.K_RETURN:
                if itemSelected == 3:
                    play = False
                if itemSelected == 2:
                    ob_game = True
                    not_game = True
                    drawButtom = True
                    if timer > 0:
                        timer -= 1
                        print(timer)
                        if timer == 0:
                            ob_game = False
                            not_game = False
                            drawButtom = False
                            timer = 2
                #if itemSelected == 0:
                    #os.startfile('C:/Users/Kurt Cobain/OneDrive/Рабочий стол/flappy bird game/main.py')




            itemSelected = itemSelected % len(menuItems)

    window.fill('white')
    window.blit(img, img_rect)

    px, py = int(WIDTH // 9), int(HEIGHT // 1.2) #90, 520

    for i in range(len(menuItems)):
        if i == itemSelected:
            #text = font.render(menuItems[i], 0, (237, 235, 130))
            #rect = text.get_rect(topleft=(px + 3, py + 3))
            #window.blit(text, rect)

            text = font.render(menuItems[i], 0, (255, 255, 255))
            rect = text.get_rect(topleft=(px - 3, py - 3))
            window.blit(text, rect)

            px += text.get_width() + 30
        else:
            text = font.render(menuItems[i], 0, (255, 255, 0))
            rect = text.get_rect(topleft=(px, py))
            window.blit(text, rect)

            px += text.get_width() + 30
        if ob_game:
            draw_ob_game()

        if drawButtom:
            draw_buttom()

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()