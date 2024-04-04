import random
from sys import exit

import pygame

from Views.TopBarView import TopBarView
from Views.GameView import GameView
from Views.KeyboardView import KeyboardView
from Views.ToastMessageView import ToastMessageView
from Views.EndGameView import EndGameView
from Utils.GameService import *
from Utils.Data import *

pygame.init()

currentRow = 0
currentCell = 0

toastMessageContent = ""
toastMessage_rect = ToastMessageView(str(toastMessageContent)).get_rect(midbottom=(240, -10))
toastMessageIsShown = False

showEndGame = False
didWin = False

keyword = random.choice(keywords)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            answer = "".join(answers[currentRow])
            print(keyword)
            if keyboardActions(x, y) != "error":
                if keyboardActions(x, y) != "submit":
                    if keyboardActions(x, y) != "delete":
                        answers[currentRow][currentCell] = keyboardActions(x, y)
                        if currentCell < 4:
                            currentCell += 1
                    elif currentCell == 4 and answers[currentRow][currentCell] != "":
                        answers[currentRow][currentCell] = ""
                    else:
                        if currentCell > 0:
                            currentCell -= 1
                        answers[currentRow][currentCell] = ""
                else:
                    if answer == keyword:
                        checkLetters()
                        didWin = True
                        showEndGame = True
                    elif len(answer) < WORD_SIZE:
                        toastMessageContent = LESS_THAN_5
                        toastMessageIsShown = True
                    elif currentRow >= WORD_SIZE:
                        checkLetters()
                        didWin = False
                        showEndGame = True
                    elif answer in wordlist:
                        checkLetters()
                        currentRow += 1
                        currentCell = 0
                    else:
                        toastMessageContent = NOT_IN_DB
                        toastMessageIsShown = True

    def checkLetters():
        for i in range(0,WORD_SIZE):
            answersColors[currentRow][i] = ProperColor(i)

    def ProperColor(idx):
        letter = answers[currentRow][idx]
        keywordList = list(keyword)

        if letter not in keywordList:
            return wrongColor
        else:
            if letter == keywordList[idx]:
                return correctColor
            else:
                return almostColor


    if toastMessage_rect.bottom <= 90 and toastMessageIsShown:
        toastMessage_rect.bottom += 12

    if toastMessage_rect.bottom >= 90:
        pygame.time.delay(3000)
        toastMessage_rect.bottom = 0
        toastMessageIsShown = False

    gameView = GameView(answers, currentCell, currentRow)

    screen.blit(TopBarView(), (0, 0))
    screen.blit(gameView[0], gameView[1])
    screen.blit(KeyboardView()[0], KeyboardView()[1])
    screen.blit(ToastMessageView(toastMessageContent), toastMessage_rect)
    if showEndGame:
        screen.blit(EndGameView(didWin, keyword), (38, 180))

    pygame.display.update()
    clock.tick(60)
