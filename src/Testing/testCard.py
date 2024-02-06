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

import unittest
from Card import Card
from RandNumberSet import RandNumberSet


class TestCard(unittest.TestCase):

    def setUp(self):
        # Create a RandNumberSet instance to use in the tests
        self.randNumSet0 = RandNumberSet(3, 40)
        self.randNumSet1 = RandNumberSet(4, 50)
        self.randNumSet2 = RandNumberSet(5, 70)
        self.randNumSet3 = RandNumberSet(6, 90)
        self.randNumSet4 = RandNumberSet(7, 130)

        # Create Card instances to use in the tests
        self.card1 = Card(0, self.randNumSet0, 3)
        self.card2 = Card(1, self.randNumSet1, 4)
        self.card3 = Card(2, self.randNumSet2, 5)
        self.card4 = Card(3, self.randNumSet3, 6)
        self.card5 = Card(4, self.randNumSet4, 7)

    def test_len(self):
        """Assert that each card's size is as expected"""
        self.assertEqual(len(self.card1), 3)
        self.assertEqual(len(self.card2), 4)
        self.assertEqual(len(self.card3), 5)
        self.assertEqual(len(self.card4), 6)
        self.assertEqual(len(self.card5), 7)

    def test_id(self):
        """Assert that each card's ID number is as expected"""
        self.assertEqual(self.card1.getID(), 0)
        self.assertEqual(self.card2.getID(), 1)
        self.assertEqual(self.card3.getID(), 2)
        self.assertEqual(self.card4.getID(), 3)
        self.assertEqual(self.card5.getID(), 4)

    def test_freeSquares(self):
        """
        Ensure that odd-sized cards have 1 "Free!" square in the center
        Also test that even-sized cards do not have a "Free!" square by examining the 2x2 region about their centers
        """
        # Test odd-sized cards
        self.assertEqual(self.card1.numberAt(1, 1), -1)
        self.assertEqual(self.card3.numberAt(2, 2), -1)
        self.assertEqual(self.card5.numberAt(3, 3), -1)

    def test_no_duplicates(self):
        """Ensure that Cards do not contain duplicate numbers"""
        for card in [self.card1, self.card2, self.card3, self.card4, self.card5]:
            seen_numbers = set()
            for row in range(len(card)):
                for col in range(len(card)):
                    number = card.numberAt(row, col)
                    if number in seen_numbers:
                        self.fail("Duplicate number {} found in Card {}".format(number, card.getID()))
                    seen_numbers.add(number)

