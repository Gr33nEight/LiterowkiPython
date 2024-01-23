from Utils.MainSettings import *


def keyboardActions(x, y):
    submit = y in range(890, 945)
    isSecondRow = y in range(721, 777)
    isOnDel = y in range(833, 889) and x in range(353, int(screenWidth) - 24)
    width = screenWidth - 48

    if y in range(665, 945):
        if submit:
            return "submit"
        elif isOnDel:
            return "delete"
        elif isSecondRow:
            for i, columnX in enumerate(range(0, int(screenWidth), 47)):
                if x in range(columnX, columnX + 47):
                    return keyboardArray[1][i]
        else:
            for i, columnX in enumerate(range(24, int(width), 47)):
                for j, rowY in enumerate(range(665, 889, 56)):
                    if x in range(columnX, columnX + 47) and y in range(rowY, rowY + 56):
                        return keyboardArray[j][i]
    else:
        return "error"
