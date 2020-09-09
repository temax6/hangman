import math
import random
import pygame
from .constants import *
pygame.init()

class WordGenButton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pygame.Surface((300, 100))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect(center = (x, y))
        self.size = self.surf.get_size()

    def change_colour(self, fill):
        self.surf.fill(fill)

class Letter(pygame.sprite.Sprite):
    def __init__(self, Let, x, y):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill(BLUE)
        self.rect = self.surf.get_rect(center = (x, y))
        self.let = FONT.render(Let, True, (WHITE))
        self.let_rect = self.let.get_rect(center = (x, y))
        self.size = (self.surf.get_size())
        self.posx = x
        self.posy = y
        self.Let = Let

    def __repr__(self):
        return str(self.Let)

    def change_colour(self, fill):
        self.surf.fill(fill)

class Underscores():
    def __init__(self, length, chosen):
        self.length = length
        self.unders = ''
        for num in (range(self.length)):
            self.unders = self.unders + '__ '
        self.rend = U_FONT.render(self.unders, True, (BLACK))
        self.rect = self.rend.get_rect(center = (int(WIDTH/2), int(HEIGHT/2 + 30)))
        self.chosen = list()
        for item in chosen:
            self.chosen.append(item)
        self.gamer = list()
        for item in chosen:
            if item not in self.gamer:
                self.gamer.append(item)
        self.corrects = 0
        self.final = list()

    def ShowLetter(self, index):
        self.crend = U_FONT.render(self.chosen[index], True, (BLACK))
        if self.length % 2 == 0:
            index_2 = (self.length/2) - index
            xpos = (WIDTH/2) - (index_2 * 58) + 23
        elif self.length % 2 == 1:
            index_2 = math.floor(self.length/2) - index
            xpos = (WIDTH/2) - (index_2 * 58) - 6
        self.crect = self.crend.get_rect(center = (int(xpos), int(HEIGHT/2 + 20)))

    def IsComplete(self, guessList):
        for item in guessList:
            if item in self.chosen:
                if item not in self.final:
                    self.final.append(item)
        if len(self.final) == len(self.gamer):
            return True
