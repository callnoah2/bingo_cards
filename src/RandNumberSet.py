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

class RandNumberSet():
    MIN_SIZE = 3
    MAX_SIZE = 16

    def __init__(self, nSize, nMax):
        self.__m_nRowPos = 0

        # __m_nSize must be between [MIN_SIZE..MAX_SIZE]
        self.__m_nSize = nSize
        if self.__m_nSize < RandNumberSet.MIN_SIZE:
            self.__m_nSize = RandNumberSet.MIN_SIZE
        elif self.__m_nSize > RandNumberSet.MAX_SIZE:
            self.__m_nSize = RandNumberSet.MAX_SIZE

        # __m_nMax must be at least __m_nSize^2
        if nMax < self.__m_nSize * self.__m_nSize:
            raise ValueError("nMax must be at least nSize^2")
        self.__m_nMax = nMax

        self.__m_arrSegments = []
        segmentSize = self.__m_nMax // self.__m_nSize
        remainder = self.__m_nMax % self.__m_nSize
        low = 1
        for segment in range(1, self.__m_nSize + 1):
            high = low + segmentSize
            if segment <= remainder:
                high += 1
            segment_numbers = set(range(low, high))
            row = []
            while len(row) < self.__m_nSize:
                num = random.randint(low, high - 1)
                if num in segment_numbers:
                    row.append(num)
                    segment_numbers.remove(num)
                if not segment_numbers:
                    break
            self.__m_arrSegments.append(row)
            low = high

    def get_column(self, col_index):
        # Shuffle the list of numbers
        segment_numbers = [row[col_index] for row in self.__m_arrSegments]
        random.shuffle(segment_numbers)

        # Remove any numbers that have already been used in previous columns
        for i in range(col_index):
            used_numbers = [row[i] for row in self.__m_arrSegments[:self.__m_nRowPos]]
            segment_numbers = list(set(segment_numbers) - set(used_numbers))

        # Take the first n numbers as the column values
        return segment_numbers[:self.__m_nMax // self.__m_nSize]
    def shuffle(self):
        """
        Shuffle each segment and reset the current row position so that
        getNextRow() will start from the top again.
        """
        for seg in self.__m_arrSegments:
            random.shuffle(seg)
        self.__m_nRowPos = 0

    def getNextRow(self):
        """
        Return the next row of Bingo numbers, or None if the RandNumberSet
        is exhausted.

        This method automatically keeps track of which row is up next
        """
        if self.__m_nRowPos >= self.__m_nSize:
            return None
        row = self.__m_arrSegments[self.__m_nRowPos]
        self.__m_nRowPos += 1
        return row

    def getSegments(self):
        """
        Accessor to private member __m_arrSegments
        """
        return self.__m_arrSegments


    def __str__(self):
        """
        Return a string representing the RandNumberSet
        """
        strs = []
        for seg in self.__m_arrSegments:
            strs.append(str(seg))
        return '\n'.join(strs)

    def __len__(self):
        """
        This dunder makes `len()` work on RandNumberSets

        The length of a RandNumberSet is equal to the number of segments
        it contains; in other words, len(RandNumberSet) == card size.
        """
        # Return the total number of unique numbers in the RandNumberSet
        return self.__m_nSize * len(self.__m_arrSegments[0]) * len(self.__m_arrSegments)

    def __getitem__(self, n):
        """
        Return the specified row of Bingo numbers, raise IndexError when out-of-bounds
        """
        if 0 <= n < self.__m_nSize:
            row = []
            for seg in self.__m_arrSegments:
                row.append(seg[n])
            return row
        else:
            raise IndexError("Index out of range")
