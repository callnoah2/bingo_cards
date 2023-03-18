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
from Deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        """
        Create no fewer than 5 Deck objects to test

        Create at least one Deck with the minimum number of Cards
        Create at least one Deck with the maximum number of Cards
        Create a mixture of large and small cards
        """
        self.deck1 = Deck(3, 5, 40, RandNumberSet(3, 40))
        self.deck2 = Deck(4, 7, 50, RandNumberSet(4, 50))
        self.deck3 = Deck(5, 3, 70, RandNumberSet(5, 70))
        self.deck4 = Deck(6, 10, 90, RandNumberSet(6, 90))
        self.deck5 = Deck(7, 2, 130, RandNumberSet(7, 130))

    def test_len(self):
        """
        Ensure that Decks contain the expected number of cards
        """
        self.assertEqual(len(self.deck1), 5)
        self.assertEqual(len(self.deck2), 7)
        self.assertEqual(len(self.deck3), 3)
        self.assertEqual(len(self.deck4), 10)
        self.assertEqual(len(self.deck5), 2)

    def test_card(self):
        """
        Ensure that specific Cards can be accessed from within a Deck

        Assert that requesting Cards at invalid indexes fails
        """
        # Test valid indexes
        deck = Deck(3, 5, 40, RandNumberSet(3, 40))
        for i in range(len(deck)):
            self.assertEqual(deck[i], deck.__getitem__(i))

        # Test invalid indexes
        deck = Deck(3, 5, 40, RandNumberSet(3, 40))
        with self.assertRaises(IndexError):
            deck[len(deck)]
        with self.assertRaises(IndexError):
            deck[-1 * (len(deck) + 1)]


if __name__ == '__main__':
    unittest.main()  	  	  
