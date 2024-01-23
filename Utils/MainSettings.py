import pygame

pygame.init()

# ---> Main settings <---

# Constants
firstRow = ["Ą", "Ć", "Ę", "Ł", "Ó", "Ś", "Ń", "Ż", "Ź"]
secondRow = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
thirdRow = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
fourthRow = ["Z", "X", "C", "V", "B", "N", "M", "DEL"]
keyboardArray = [firstRow, secondRow, thirdRow, fourthRow]

#Measurements
screenWidth = 470.4
screenHeight = 1012.8
rectSize = 75
letterHeight = 55
letterWidth = 45

# Colors
backgroundColor = (21, 18, 19)
correctColor = (132, 220, 207)
almostColor = (239, 98, 108)
wrongColor = (85, 79, 80)
textColor = (232, 231, 231)
greyColor = (148, 140, 141)

# Fonts
largeFont = pygame.font.Font('../font/rubik_bold.ttf', 42)
mediumFont = pygame.font.Font('../font/rubik_medium.ttf', 34)
smallFont = pygame.font.Font('../font/rubik_medium.ttf', 26)
verySmallFont = pygame.font.Font('../font/rubik_medium.ttf', 20)

# Size
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Name
pygame.display.set_caption("Literówki")

# Icon
icon = pygame.image.load('../logo.png')
pygame.display.set_icon(icon)

# Clock
clock = pygame.time.Clock()

# Background
screen.fill(backgroundColor)

# -----------------------
