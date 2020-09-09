import string
import random
import pygame
from __hangman.constants import *
from __hangman.classes import *
pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
logo = pygame.image.load("__hangman\hangman32x32.png")
pygame.display.set_icon(logo)
pygame.display.set_caption('Hangman')


def main():
    WIN.fill(WHITE)
    running = True
    onLoad = True
    genWord = True
    gameOver = False
    clock = pygame.time.Clock()
    wgButton = WordGenButton(WIDTH/2, HEIGHT/2)
    playAgain = WordGenButton(WIDTH/2, 600)

    guessed = list()
    alphabet = list()

    if 1 == 1:
        gap = 60
        x_coord = 500
        A = Letter('A', (WIDTH/2) - gap*6, x_coord)
        B = Letter('B', (WIDTH/2) - gap*5, x_coord)
        C = Letter('C', (WIDTH/2) - gap*4, x_coord)
        D = Letter('D', (WIDTH/2) - gap*3, x_coord)
        E = Letter('E', (WIDTH/2) - gap*2, x_coord)
        F = Letter('F', (WIDTH/2) - gap, x_coord)
        G = Letter('G', (WIDTH/2), x_coord)
        H = Letter('H', (WIDTH/2) + gap, x_coord)
        I = Letter('I', (WIDTH/2) + gap*2, x_coord)
        J = Letter('J', (WIDTH/2) + gap*3, x_coord)
        K = Letter('K', (WIDTH/2) + gap*4, x_coord)
        L = Letter('L', (WIDTH/2) + gap*5, x_coord)
        M = Letter('M', (WIDTH/2) + gap*6, x_coord)

        N = Letter('N', (WIDTH/2) - gap*6, x_coord+gap)
        O = Letter('O', (WIDTH/2) - gap*5, x_coord+gap)
        P = Letter('P', (WIDTH/2) - gap*4, x_coord+gap)
        Q = Letter('Q', (WIDTH/2) - gap*3, x_coord+gap)
        R = Letter('R', (WIDTH/2) - gap*2, x_coord+gap)
        S = Letter('S', (WIDTH/2) - gap, x_coord+gap)
        T = Letter('T', (WIDTH/2), x_coord+gap)
        U = Letter('U', (WIDTH/2) + gap, x_coord+gap)
        V = Letter('V', (WIDTH/2) + gap*2, x_coord+gap)
        W = Letter('W', (WIDTH/2) + gap*3, x_coord+gap)
        X = Letter('X', (WIDTH/2) + gap*4, x_coord+gap)
        Y = Letter('Y', (WIDTH/2) + gap*5, x_coord+gap)
        Z = Letter('Z', (WIDTH/2) + gap*6, x_coord+gap)


        letters = pygame.sprite.Group()
        letters.add(A)
        letters.add(B)
        letters.add(C)
        letters.add(D)
        letters.add(E)
        letters.add(F)
        letters.add(G)
        letters.add(H)
        letters.add(I)
        letters.add(J)
        letters.add(K)
        letters.add(L)
        letters.add(M)

        letters.add(N)
        letters.add(O)
        letters.add(P)
        letters.add(Q)
        letters.add(R)
        letters.add(S)
        letters.add(T)
        letters.add(U)
        letters.add(V)
        letters.add(W)
        letters.add(X)
        letters.add(Y)
        letters.add(Z)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if onLoad == True:
            WIN.blit(wgButton.surf, wgButton.rect)
            wgString = FONT.render('Generate Word', True, (WHITE))
            wgRect = wgString.get_rect(center = (int(WIDTH/2), int(HEIGHT/2)))
            WIN.blit(wgString, wgRect)
            wgSize = wgButton.size

        mouse = pygame.mouse.get_pos()
        if mouse[0] > (WIDTH - wgSize[0])/2 and mouse[0] < (WIDTH + wgSize[0])/2 \
            and mouse[1] > (HEIGHT - wgSize[1])/2 and mouse[1] < (HEIGHT + wgSize[1])/2:
            wgButton.change_colour(GREY)
            if event.type == pygame.MOUSEBUTTONDOWN:
                WIN.fill(WHITE)
                onLoad = False
        else:
            wgButton.change_colour(GREEN)

        if onLoad == False and genWord == True:
            with open('__hangman/words.txt') as f:
                word_list = [line.rstrip('\n') for line in f]
                choice = random.choice(word_list)
                underScr = Underscores(len(choice), choice)
                print(choice)
                current_lives = 6
                genWord = False

        if gameOver == False and genWord == False:
            WIN.blit(underScr.rend, underScr.rect)
            for letter in letters:
                alphabet.append(letter.Let)
                WIN.blit(letter.surf, letter.rect)
                WIN.blit(letter.let, letter.let_rect)
                if underScr.IsComplete(guessed) == True:
                    gameOver = True
                if letter.Let not in guessed:
                    if mouse[0] > (letter.posx - (letter.size[0]/2)) and mouse[0] < (letter.posx + (letter.size[0]/2)) \
                        and mouse[1] > (letter.posy - (letter.size[1]/2)) and mouse[1] < (letter.posy + (letter.size[1]/2)):
                        letter.change_colour(GREY)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            index = alphabet.index(letter.Let)
                            guessed.append(alphabet.pop(index))
                            if letter.Let in choice:
                                counter = (choice.count(letter.Let))
                                while counter > 0:
                                    ind = [i for i, n in enumerate(choice) if n == letter.Let][counter-1]
                                    underScr.ShowLetter(ind)
                                    WIN.blit(underScr.crend, underScr.crect)
                                    counter -= 1
                            if letter.Let not in choice:
                                current_lives -= 1

                    else:
                        letter.change_colour(BLUE)

        if gameOver == True:
            WIN.fill(WHITE)
            final_i = 0
            for letter in underScr.chosen:
                underScr.ShowLetter(final_i)
                WIN.blit(underScr.crend, underScr.crect)
                final_i += 1
            
            niceString = FONT.render('Well Done!', True, (BLUE))
            niceRect = niceString.get_rect(center = (int(WIDTH/2), int(300)))
            WIN.blit(niceString, niceRect)

            
            WIN.blit(playAgain.surf, playAgain.rect)
            paString = FONT.render('Play Again?', True, (WHITE))
            paRect = paString.get_rect(center = (int(WIDTH/2), int(600)))
            WIN.blit(paString, paRect)
            paSize = playAgain.size

            mouse = pygame.mouse.get_pos()
            if mouse[0] > (WIDTH - paSize[0])/2 and mouse[0] < (WIDTH + paSize[0])/2 \
                and mouse[1] > (600 - (paSize[1]/2)) and mouse[1] < (600 + (paSize[1]/2)):
                playAgain.change_colour(GREY)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
            else:
                playAgain.change_colour(GREEN)
                

        pygame.display.update()
    pygame.quit()

main()