from random import randint
class NumberPicker:
    colNames = list("BINGOLARDYPEZMUX")
    used = []

    def __init__(self, maxNum, cardSize):
        self.maxNum = maxNum
        self.cardSize = cardSize

    def pickNum(self):
        while True:
            num = randint(1, self.maxNum)
            if num not in NumberPicker.used:
                NumberPicker.used.append(num)
                return num

    def getCol(self, num):
        col_index = (num - 1) // ((self.maxNum // self.cardSize) + 1)
        return self.colNames[col_index]

    def getNum(self):
        while True:
            num = self.pickNum()
            if num:
                return num

    def __str__(self):
        num = self.getNum()
        col = self.getCol(num)
        return f"{col}{num:02}"
