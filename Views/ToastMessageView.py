from Utils.MainSettings import *
from Views.GameView import draw_rounded_rect, draw_rounded_border

def ToastMessageView(message):
    view = pygame.Surface((screenWidth - 60, 80))
    mess = verySmallFont.render(message, False, backgroundColor)
    rect = pygame.Rect(
        0, 0,
        screenWidth-60, 80
    )
    border = pygame.Rect(
        0, 0,
        screenWidth - 60, 80
    )
    draw_rounded_rect(view, rect, greyColor, 5)
    draw_rounded_border(view, border, almostColor, 5, 2)
    view.blit(mess, (20, 30))
    return view
