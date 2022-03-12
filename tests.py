import unittest

from translator import englishtofrench, englishtogerman

class TestTranslator(unittest.TestCase):
    def test_englishtofrench_null_input(self):
        self.assertEqual(englishtofrench(), None)

    def test_englishtofrench_hello_world_not_null(self):
        self.assertNotEqual(englishtofrench("Hello"), None)
    
    def test_englishtofrench_hello_world_str(self):
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
    
    def test_englishtogerman_null_input(self):
        self.assertEqual(englishtogerman(), None)

    def test_englishtogerman_hello_world_not_null(self):
        self.assertNotEqual(englishtogerman("Hello"), None)
    
    def test_englishtogerman_hello_world_str(self):
        self.assertEqual(englishtogerman("Hello"), "Hallo")

if __name__ == "__main__":
    unittest.main()
