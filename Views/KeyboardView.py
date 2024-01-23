import pygame

from Utils.MainSettings import *
from Views.GameView import draw_rounded_rect

pygame.init()


def KeyboardView():
    view = pygame.Surface((screenWidth, screenHeight / 3.5))
    view.fill(backgroundColor)
    view_rect = view.get_rect(center=(screenWidth / 2, screenHeight / 1.25))
    for i, row in enumerate(keyboardArray):
        for j, letter in enumerate(row):
            letterCell = LetterCell(str(letter))
            x = j * screenWidth / len(row)
            y = i * 57
            view.blit(letterCell, (int(proper_x(x, i)), y))
    view.blit(EnterButton(), (0, 229))
    return view, view_rect

def proper_x(x, i):
    if i % 2 == 0:
        return (x * 0.9) + 25
    elif i == 1:
        return x
    else:
        return (x*0.8) + 25


def LetterCell(content):
    view = pygame.Surface((rectSize, rectSize))
    view.fill(backgroundColor)
    rect = pygame.Rect(
        0, 0,
        letterWidth if len(content) == 1 else letterWidth*1.6,
        letterHeight
    )
    draw_rounded_rect(view, rect, greyColor, 5)
    letter = smallFont.render(str(content), False, textColor)
    letter_rect = view.get_rect(center=(50, 47))
    view.blit(letter, letter_rect)
    return view

def EnterButton():
    view = pygame.Surface((screenWidth, rectSize))
    view.fill(backgroundColor)
    rect = pygame.Rect(0, 0, screenWidth, letterHeight)
    draw_rounded_rect(view, rect, greyColor, 5)
    letter = smallFont.render("ENTER", False, textColor)
    letter_rect = view.get_rect(center=(screenWidth/1.1, letterHeight/1.2))
    view.blit(letter, letter_rect)
    return view
