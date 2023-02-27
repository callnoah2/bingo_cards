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
from Menu import Menu  	  	  
from MenuOption import MenuOption  	  	  


class TestMenu(unittest.TestCase):  	  	  
    def test_add_options(self):  	  	  
        """Ensure that options can be added to a Menu"""  	  	  
        menu = Menu("Adding Options")  	  	  
        self.assertEqual(len(menu), 0)  	  	  
        menu += MenuOption("A", "Test option A")  	  	  
        self.assertEqual(len(menu), 1)  	  	  
        menu += MenuOption("B", "Test option B")  	  	  
        self.assertEqual(len(menu), 2)  	  	  
        menu += MenuOption("C", "Test option C")  	  	  
        self.assertEqual(len(menu), 3)  	  	  
        menu += MenuOption("D", "Test option D")  	  	  
        self.assertEqual(len(menu), 4)  	  	  
        menu += MenuOption("E", "Test option E")  	  	  
        self.assertEqual(len(menu), 5)  	  	  

    def test_get_options(self):  	  	  
        """Ensure that menu options can be retrieved from Menus"""  	  	  
        menu = Menu("Getting Options")  	  	  
        menu += MenuOption("A", "Test option A")  	  	  
        menu += MenuOption("B", "Test option B")  	  	  
        menu += MenuOption("C", "Test option C")  	  	  
        menu += MenuOption("D", "Test option D")  	  	  
        menu += MenuOption("E", "Test option E")  	  	  

        opt = menu[0]  	  	  
        self.assertEqual(opt.getCommand(), "A")  	  	  
        self.assertEqual(opt.getDescription(), "Test option A")  	  	  

        opt = menu[1]  	  	  
        self.assertEqual(opt.getCommand(), "B")  	  	  
        self.assertEqual(opt.getDescription(), "Test option B")  	  	  

        opt = menu[2]  	  	  
        self.assertEqual(opt.getCommand(), "C")  	  	  
        self.assertEqual(opt.getDescription(), "Test option C")  	  	  

        opt = menu[3]  	  	  
        self.assertEqual(opt.getCommand(), "D")  	  	  
        self.assertEqual(opt.getDescription(), "Test option D")  	  	  

        opt = menu[4]  	  	  
        self.assertEqual(opt.getCommand(), "E")  	  	  
        self.assertEqual(opt.getDescription(), "Test option E")  	  	  

        self.assertRaises(IndexError, menu.__getitem__, 5)  	  	  
        self.assertRaises(IndexError, menu.__getitem__, 6)  	  	  
        self.assertRaises(IndexError, menu.__getitem__, -1)  	  	  
        self.assertRaises(IndexError, menu.__getitem__, -2)  	  	  

    def test_is_valid_command(self):  	  	  
        """Ensure Menu can distinguish bad commands from the good ones"""  	  	  
        menu = Menu("Validate Commands")  	  	  
        menu += MenuOption("A", "Test option A")  	  	  
        menu += MenuOption("B", "Test option B")  	  	  
        menu += MenuOption("C", "Test option C")  	  	  
        menu += MenuOption("D", "Test option D")  	  	  
        menu += MenuOption("E", "Test option E")  	  	  
        self.assertTrue(menu.isValidCommand("A"))  	  	  
        self.assertTrue(menu.isValidCommand("B"))  	  	  
        self.assertTrue(menu.isValidCommand("C"))  	  	  
        self.assertTrue(menu.isValidCommand("D"))  	  	  
        self.assertTrue(menu.isValidCommand("E"))  	  	  

        self.assertTrue(menu.isValidCommand("a"))  	  	  
        self.assertTrue(menu.isValidCommand("b"))  	  	  
        self.assertTrue(menu.isValidCommand("c"))  	  	  
        self.assertTrue(menu.isValidCommand("d"))  	  	  
        self.assertTrue(menu.isValidCommand("e"))  	  	  

        self.assertFalse(menu.isValidCommand("x"))  	  	  
        self.assertFalse(menu.isValidCommand("X"))  	  	  
        self.assertFalse(menu.isValidCommand("Y"))  	  	  
        self.assertFalse(menu.isValidCommand("Z"))  	  	  
        self.assertFalse(menu.isValidCommand("?"))  	  	  


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
