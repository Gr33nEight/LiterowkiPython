import pygame

from Utils.MainSettings import *
from Views.GameView import draw_rounded_rect, draw_rounded_border

def EndGameView(didWin, keyword):
    view = pygame.Surface((screenWidth-80, screenHeight/3))
    mess = largeFont.render(
        "WYGRAŁEŚ!" if didWin else "PRZEGRAŁEŚ!", False,
        correctColor if didWin else almostColor
    )
    secondMess = smallFont.render(
        "Hasło to: " + str(keyword), False, textColor
    )
    rect = pygame.Rect(
        0, 0,
        screenWidth-80, screenHeight/3
    )
    border = pygame.Rect(
        0, 0,
        screenWidth-80, screenHeight/3
    )
    draw_rounded_rect(view, rect, backgroundColor, 15)
    draw_rounded_border(view, border, correctColor if didWin else almostColor, 15, 10)
    view.blit(mess, (45, 85))
    view.blit(secondMess, (85, 200))
    return view