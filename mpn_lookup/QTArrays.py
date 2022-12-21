from .qtfile import qt2kArray, qtArray, qtLEGIOArray


class QTArray:
    def __init__(self):
        pass


def getQT2Kmpn(inPosLarge, inPosSmall):
    if type(inPosLarge) != int:
        inPosLarge = int(inPosLarge)
        inPosSmall = int(inPosSmall)

    if inPosLarge not in range(0,50):
        print("value not valid, must be between 0->49 inclusive")
        return

    elif inPosSmall not in range(0,49):
        print("value not valid, must be between 0->48 inclusive")
        return
    else:
        return qt2kArray[inPosLarge*49 + inPosSmall]


def getQTmpn(inPos):
    if inPos not in range(0,52):
        print("value not valid, must be between 0->51 inclusive")
        return
    else:
        return qtArray[inPos]


def getQTLEGIOmpn(inPosSmall, inPosLarge):
    if inPosLarge not in range(0,7):
        print("value not valid, must be between 0->49 inclusive")
        return

    elif inPosSmall not in range(0,91):
        print("value not valid, must be between 0->48 inclusive")
        return
    else:
        return qtLEGIOArray[inPosSmall][inPosLarge]
