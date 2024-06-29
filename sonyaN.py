import pygame
import os

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((550,700))

geroy = pygame.Rect(0, 0, 30, 30)

go_right = False
go_left = False
go_up = False
go_down = False

dir_path = os.path.dirname(__file__)
img_path = os.path.abspath(dir_path + "/textures")

labirint_cookiefall = pygame.image.load(img_path + "/labirint_cookiefall.png")
Paska = pygame.image.load(img_path + "/Paska.png")
wall2 = pygame.image.load(img_path + "/wall2.png")
sunduk = pygame.image.load(img_path + "/sunduk.png")
hero = pygame.transform.scale(pygame.image.load(img_path + "/yellowchelovek.png"), (30,30))

# labirint_cookiefall = 1
# Paska = 2
# wall2 = 3
# sunduk = 4
# hero = 9

textures = [
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,2,1,2,1,2,1,2,1,1],
    [1,2,3,1,3,1,3,1,2,1,1],
    [1,2,4,1,4,1,4,1,2,1,1],
    [1,1,1,3,2,1,3,2,1,1,1],
    [1,1,2,1,2,1,2,1,2,1,1],
    [1,2,3,1,2,3,1,2,3,1,1],
    [1,2,4,1,4,1,4,1,4,1,1],
    [1,3,2,1,2,3,2,2,3,1,1],
    [1,1,2,1,2,1,2,1,2,1,1],
    [1,2,3,1,3,1,3,1,2,1,1],
    [1,2,4,1,4,1,4,1,2,1,1],
    [1,3,3,3,2,1,3,2,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1]
]

rects = []
rects_textures = []

bad_rects = []
good_rects = []

x = 0
y = 0

for texture in textures:
    for i in texture:
        kvadrat = pygame.Rect(x, y, 50, 50)
        rects.append(kvadrat)
        rects_textures.append(i)
        if i == 2 or i == 3:
            bad_rects.append(kvadrat)
        if i == 4:
            good_rects.append(kvadrat)
        x += 50
    y += 50
    x = 0

font = pygame.font.SysFont("Arial", 50)
text = font.render("YOU WIN", True, (0,255,0))

ochki = 0

game = True

while game:

    display.fill((180, 127, 127))

    for i in range (len(rects)):
        if rects_textures[i] == 1:
            display.blit(labirint_cookiefall, rects[i])
        if rects_textures[i] == 2:
            display.blit(Paska, rects[i])
        if rects_textures[i] == 3:
            display.blit(wall2, rects[i])
        if rects_textures[i] == 4:
            display.blit(sunduk, rects[i])
       
    display.blit(hero, geroy)

    for bad in bad_rects:
        if geroy.colliderect(bad):
            geroy.x = 0
            geroy.y = 0

    for good in good_rects:
        if geroy.colliderect(good):
            ochki += 1
            good_rects.remove(good)
            rects_textures[rects.index(good)] = 1

    if ochki == 10:
        display.fill((0, 0, 0))
        display.blit(text, (175, 325))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                go_right = True
            if event.key == pygame.K_a:
                go_left = True
            if event.key == pygame.K_w:
                go_up = True
            if event.key == pygame.K_s:
                go_down = True
            if event.key == pygame.K_SPACE:
                print(ochki)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_w:
                go_up = False
            if event.key == pygame.K_s:
                go_down = False

    if go_right == True:
        geroy.x += 4
    if go_left == True:
        geroy.x -= 4
    if go_up == True:
        geroy.y -= 4
    if go_down == True:
        geroy.y += 4

    pygame.display.flip()
    clock.tick(60)
