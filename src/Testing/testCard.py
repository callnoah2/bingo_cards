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
        """  	  	  
        Create no fewer than 5 Card objects to test  	  	  

        Create a mixture of odd and even-sized cards  	  	  
        """  	  	  
        pass  	  	  


    def test_len(self):  	  	  
        """Assert that each card's size is as expected"""  	  	  
        self.assertTrue(False, "TODO: implement this test")  	  	  

    def test_id(self):  	  	  
        """Assert that each card's ID number is as expected"""  	  	  
        self.assertTrue(False, "TODO: implement this test")  	  	  

    def test_freeSquares(self):  	  	  
        """  	  	  
        Ensure that odd-sized cards have 1 "Free!" square in the center  	  	  
        Also test that even-sized cards do not have a "Free!" square by examining the 2x2 region about their centers  	  	  
        """  	  	  
        self.assertTrue(False, "TODO: implement this test")  	  	  

    def test_no_duplicates(self):  	  	  
        """Ensure that Cards do not contain duplicate numbers"""  	  	  
        # Hint: look at how TestRandNumberSet.test_noDuplicates works  	  	  
        self.assertTrue(False, "TODO: implement this test")  	  	  


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
