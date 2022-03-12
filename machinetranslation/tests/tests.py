import unittest
import os, sys
sys.path.insert(0, os.getcwd()) 

import translator

class TestTranslator(unittest.TestCase):
    def test_englishtofrench_null_input(self):
        self.assertEqual(translator.englishtofrench(), None)

    def test_englishtofrench_hello_world_not_null(self):
        self.assertNotEqual(translator.englishtofrench("Hello"), None)
    
    def test_englishtofrench_hello_world_str(self):
        self.assertEqual(translator.englishtofrench("Hello"), "Bonjour")
    
    def test_englishtogerman_null_input(self):
        self.assertEqual(translator.englishtogerman(), None)

    def test_englishtogerman_hello_world_not_null(self):
        self.assertNotEqual(translator.englishtogerman("Hello"), None)
    
    def test_englishtogerman_hello_world_str(self):
        self.assertEqual(translator.englishtogerman("Hello"), "Hallo")

if __name__ == "__main__":
    unittest.main()
