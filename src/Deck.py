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
    def __init__(self, nCardSize, nNumCards, nMaxNum):  	  	  
        """  	  	  
        Deck constructor  	  	  
        """  	  	  
        pass  	  	  

    def __len__(self):  	  	  
        """  	  	  
        Return an integer: the number of cards in this deck  	  	  

        This method was called `getSize` in the C++ version  	  	  
        """  	  	  
        pass  	  	  

    def __getitem__(self, nIdx):  	  	  
        """  	  	  
        Return Card N from the Deck  	  	  

        This method was called `operator[]` in the C++ version  	  	  
        """  	  	  
        pass  	  	  

    def __str__(self):  	  	  
        """  	  	  
        Return a string: return the entire Deck as a string  	  	  

        This is basically equivalent to the `operator<<` method in the C++ version  	  	  
        """  	  	  
        pass  	  	  
