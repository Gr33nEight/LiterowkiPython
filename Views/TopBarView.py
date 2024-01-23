from Utils.MainSettings import *
pygame.init()

def TopBarView():
    view = pygame.Surface((screenWidth, 100))
    view.fill(backgroundColor)
    appName = largeFont.render("LITERÓWKI", False, textColor)
    text_rect = appName.get_rect(center=(screenWidth / 2, 50))
    view.blit(appName, text_rect)
    return view