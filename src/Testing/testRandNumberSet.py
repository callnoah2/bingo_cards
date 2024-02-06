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
from RandNumberSet import RandNumberSet  	  	  


class TestRandNumberSet(unittest.TestCase):  	  	  
    def setUp(self):  	  	  
        self.ns3 = RandNumberSet(3, 19)  	  	  
        self.ns4 = RandNumberSet(4, 32)  	  	  
        self.ns8 = RandNumberSet(8, 192)  	  	  
        self.ns16 = RandNumberSet(16, 8192)  	  	  

    def test_len(self):  	  	  
        """Ensure that a RandNumberSet's length is as expected"""  	  	  
        self.assertEqual(len(self.ns3), 3)  	  	  
        self.assertEqual(len(self.ns4), 4)  	  	  
        self.assertEqual(len(self.ns8), 8)  	  	  
        self.assertEqual(len(self.ns16), 16)  	  	  

    def test_getitem(self):  	  	  
        """  	  	  
        Ensure that RandNumberSet  	  	  
        * retrieves the same data each time the same row is requested  	  	  
        * raises IndexError for requests of out-of-bounds rows  	  	  
        * shuffling the RandNumberSet does not affect the boundaries  	  	  
        """  	  	  
        for i in range(len(self.ns8)):  	  	  
            self.assertEqual(self.ns8[i], self.ns8[i])  	  	  
        self.ns8.shuffle()  	  	  
        for i in range(len(self.ns8)):  	  	  
            self.assertEqual(self.ns8[i], self.ns8[i])  	  	  

        for i in range(len(self.ns16)):  	  	  
            self.assertEqual(self.ns16[i], self.ns16[i])  	  	  
        self.ns16.shuffle()  	  	  
        for i in range(len(self.ns16)):  	  	  
            self.assertEqual(self.ns16[i], self.ns16[i])  	  	  

        for _ in range(3):  	  	  
            self.assertRaises(IndexError, self.ns4.__getitem__, -1)  	  	  
            self.assertRaises(IndexError, self.ns4.__getitem__, -10)  	  	  
            self.assertRaises(IndexError, self.ns4.__getitem__, 4)  	  	  
            self.assertRaises(IndexError, self.ns4.__getitem__, 5)  	  	  
            self.assertRaises(IndexError, self.ns4.__getitem__, 6)  	  	  
            self.assertRaises(IndexError, self.ns4.__getitem__, 3000)  	  	  
            self.ns4.shuffle()  	  	  
            self.assertRaises(IndexError, self.ns16.__getitem__, -1)  	  	  
            self.assertRaises(IndexError, self.ns16.__getitem__, -10)  	  	  
            self.assertRaises(IndexError, self.ns16.__getitem__, 17)  	  	  
            self.assertRaises(IndexError, self.ns16.__getitem__, 18)  	  	  
            self.assertRaises(IndexError, self.ns16.__getitem__, 19)  	  	  
            self.assertRaises(IndexError, self.ns16.__getitem__, 3000)  	  	  
            self.ns16.shuffle()  	  	  

    def test_getNextRow(self):  	  	  
        """  	  	  
        Ensure that a RandNumberSet's .getNextRow() method  	  	  
        * returns `None` when exhausted  	  	  
        * can be reset by `.shuffle()`  	  	  
        * retrieves different rows each time it's called  	  	  
        """  	  	  
        # In my implementation, once a RandNumberSet is exhausted, repeated invocations of `.getNextRow()` returns None  	  	  
        for i in range(len(self.ns16)):  	  	  
            self.assertIsNotNone(self.ns16.getNextRow())  	  	  
        self.assertIsNone(self.ns16.getNextRow())  	  	  

        self.ns16.shuffle()  	  	  

        for i in range(len(self.ns16)):  	  	  
            self.assertIsNotNone(self.ns16.getNextRow())  	  	  
        self.assertIsNone(self.ns16.getNextRow())  	  	  

        self.assertNotEqual(self.ns8.getNextRow(), self.ns8.getNextRow())  	  	  
        self.assertNotEqual(self.ns8.getNextRow(), self.ns8.getNextRow())  	  	  
        self.assertNotEqual(self.ns8.getNextRow(), self.ns8.getNextRow())  	  	  
        self.assertNotEqual(self.ns8.getNextRow(), self.ns8.getNextRow())  	  	  
        self.assertIsNone(self.ns8.getNextRow())  	  	  

    def test_noDuplicates(self):  	  	  
        """Ensure that a RandNumberSet contains no duplicates"""  	  	  

        # Here I use a set to quickly and easily detect duplicates:  	  	  
        # First, create a list of all the numbers yielded from a RandNumberSet  	  	  
        # Then convert that list into a set  	  	  
        # If the length of the list is not equal to that of the set, then there  	  	  
        # must have been duplicates in the list  	  	  
        seen = set()  	  	  
        for segment in self.ns3.getSegments():  	  	  
            for n in segment:  	  	  
                self.assertNotIn(n, seen)  	  	  
                seen.add(n)  	  	  


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
