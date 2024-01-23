import pygame
from Utils.Data import *
from Utils.MainSettings import *

pygame.init()


def GameView(answers, currentCell, currentRow):
    view = pygame.Surface((screenWidth - 25, screenHeight / 2))
    view.fill(backgroundColor)
    view_rect = view.get_rect(center=(screenWidth / 1.88, screenHeight / 2.8))
    for row in range(0, 6):
        for cell in range(0, 5):
            isCurrent = currentCell == cell and currentRow == row
            color = answersColors[row][cell]
            cellView = CellView(answers[row][cell], isCurrent, color)
            view.blit(cellView, (cell * 84, row * 84))
    return view, view_rect


def CellView(letter, isCurrent, color):
    resizableRectSize = rectSize - 15 if isCurrent else rectSize
    changableRectPos = 7.5 if isCurrent else 0
    resizableBorderSize = rectSize if isCurrent else rectSize - 5
    changableBorderPos = 0 if isCurrent else 5
    rectBorder = pygame.Rect(
        changableBorderPos,
        changableBorderPos,
        resizableBorderSize,
        resizableBorderSize
    )
    view = pygame.Surface((
        rectSize,
        rectSize
    ))
    view.fill(backgroundColor)
    rect = pygame.Rect(
        changableRectPos,
        changableRectPos,
        resizableRectSize,
        resizableRectSize,
    )
    draw_rounded_border(view, rectBorder, textColor, 5, 3)
    draw_rounded_rect(view, rect, color, 5)

    letter = mediumFont.render(str(letter), False, textColor)
    letter_rect = view.get_rect(center=(62, 54))
    view.blit(letter, letter_rect)
    return view


def draw_rounded_rect(surface, rect, color, radius):
    corner_radius = int(radius)
    pygame.draw.rect(surface, color, rect, 0, corner_radius)


def draw_rounded_border(surface, rect, color, radius, width):
    corner_radius = int(radius)
    pygame.draw.rect(surface, color, rect, width, corner_radius)
