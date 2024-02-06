
from Card import Card

class Deck():
    def __init__(self, nCardSize, nNumCards, nMaxNum, rand_num_set):
        self.__m_cards = []
        self.__m_size = nCardSize
        self.__m_max_num = nMaxNum
        self.__m_num_cards = nNumCards

        for i in range(nNumCards):
            card = Card(i, rand_num_set, nCardSize)
            self.__m_cards.append(card)

    def __len__(self):
        return len(self.__m_cards)

    def __getitem__(self, nIdx):
        return self.__m_cards[nIdx]

    def __str__(self):
        outpt = ""
        for card in self.__m_cards:
            outpt += str(card)
            outpt += "\n"
        return outpt
    def __maxNum__(self):
        return self.__m_max_num
    def getSize(self):
        return self.__m_size
