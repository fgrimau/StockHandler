import pygame
from pygame.locals import *
from functions import *
from db import *

#SCREEN
SCREEN_X = 1024
SCREEN_Y = 768
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

#FONTS
fonts = {}
for x in [14, 20, 25, 30, 35, 50, 75, 100]:
    fonts[str(x)] = pygame.font.Font('fonts/BebasNeue-Regular.ttf', x)

urlabBanner = CreateBanner(fonts, SCREEN_X)

#IMAGES MADE BY THE COMPUTER
background = pygame.Surface((SCREEN_X, SCREEN_Y))
background.fill((255, 255, 255))

#HANDLERS
mainMenuHandlers = ["Acheter", "Remplir", "Stock", "BDD", "", "Mon solde"]
buyMenuHandlers  = ["Annuler dernier", "", "Retour", "Vider", "", "Terminer"]

#DATABASE
dataBase = DataBase('data/db.json')
dataBase.add("Club-Mate", "azerty", 2, "imgs/products/club_mate.png")
dataBase.save()

#Menus
