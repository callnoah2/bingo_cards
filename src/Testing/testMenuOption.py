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

from MenuOption import MenuOption  	  	  


class TestMenuOption(unittest.TestCase):  	  	  

    def setUp(self):  	  	  
        """Create no fewer than 5 MenuOption objects to test"""  	  	  
        self.a = MenuOption("A", "Test option A")  	  	  
        self.b = MenuOption("B", "Test option B")  	  	  
        self.c = MenuOption("C", "Test option C")  	  	  
        self.d = MenuOption("D", "Test option D")  	  	  
        self.e = MenuOption("E", "Test option E")  	  	  

    def test_chCommand(self):  	  	  
        """Ensure each option's letter char is set correctly"""  	  	  
        self.assertEqual(self.a.getCommand(), "A")  	  	  
        self.assertEqual(self.b.getCommand(), "B")  	  	  
        self.assertEqual(self.c.getCommand(), "C")  	  	  
        self.assertEqual(self.d.getCommand(), "D")  	  	  
        self.assertEqual(self.e.getCommand(), "E")  	  	  

    def test_szDescription(self):  	  	  
        """Ensure each option's description is set correctly"""  	  	  
        self.assertEqual(self.a.getDescription(), "Test option A")  	  	  
        self.assertEqual(self.b.getDescription(), "Test option B")  	  	  
        self.assertEqual(self.c.getDescription(), "Test option C")  	  	  
        self.assertEqual(self.d.getDescription(), "Test option D")  	  	  
        self.assertEqual(self.e.getDescription(), "Test option E")  	  	  

    def test_str(self):  	  	  
        """Ensure the __str__ dunder works correctly"""  	  	  
        self.assertEqual(str(self.a), "\x1b[1;33mA\x1b[0m) \x1b[1;36mTest option A\x1b[0m")  	  	  
        self.assertEqual(str(self.b), "\x1b[1;33mB\x1b[0m) \x1b[1;36mTest option B\x1b[0m")  	  	  
        self.assertEqual(str(self.c), "\x1b[1;33mC\x1b[0m) \x1b[1;36mTest option C\x1b[0m")  	  	  
        self.assertEqual(str(self.d), "\x1b[1;33mD\x1b[0m) \x1b[1;36mTest option D\x1b[0m")  	  	  
        self.assertEqual(str(self.e), "\x1b[1;33mE\x1b[0m) \x1b[1;36mTest option E\x1b[0m")  	  	  


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
