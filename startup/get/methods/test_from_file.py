import unittest
from startup.get.methods.from_file import get_data_from_file

class TestGetDataFromFile(unittest.TestCase):
    def test_get(self):
        self.assertFalse(get_data_from_file('not_a_file')[0])
        self.assertTrue(get_data_from_file('/home/denis/projects/test/data/pep.txt')[0])

if __name__ == '__main__':
    unittest.main()
