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

import random

class Card():
    COLUMN_NAMES = list("BINGOLARDYPEZMUX")

    def __init__(self, nId, randNumSet):
        self.id = nId
        self.numbers = []
        for i, col in enumerate(self.COLUMN_NAMES):
            col_nums = random.sample(range(randNumSet[i]), 5)
            self.numbers.append(col_nums)

    def getID(self):
        return self.id

    def numberAt(self, nRow, nCol):
        return self.numbers[nCol][nRow]

    def __len__(self):
        len(self.numbers)

    def __str__(self, nID):
        # Get the size of the card
        size = len(self)

        # Create the header row with column names
        header = "Card #{}\n  ".format(nID)
        for column in self.COLUMN_NAMES[:size]:
            header += "{:^5}".format(column)
        header += "\n"

        # Create the separator row
        separator = "+-----" * size + "+\n"

        # Create the rows with numbers
        rows = ""
        for row in range(size):
            row_str = "|"
            for col in range(size):
                value = self.numberAt(row, col)
                if value == -1:
                    value_str = "FREE!"
                else:
                    value_str = str(value).center(5)
                row_str += value_str + "|"
            rows += row_str + "\n"

        # Combine everything into the final string
        return header + separator + rows + separator