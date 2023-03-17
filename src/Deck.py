#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

from Card import Card  	  	  
from RandNumberSet import RandNumberSet

class Deck():
    def __init__(self, nCardSize, nNumCards, nMaxNum, rand_num_set):
        self.__m_cards = []
        self.__m_size = nCardSize
        self.__m_max_num = nNumCards
        self.__m_num_cards = nMaxNum

        for i in range(nNumCards):
            card = Card(i, rand_num_set, nCardSize)
            print(f"Adding card {i} to deck")
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