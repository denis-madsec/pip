import unittest
import requests
from startup.get.methods.from_web import get_data_from_web

class TestGetDataFromWeb(unittest.TestCase):
    def test_get(self):

        with self.assertRaises(requests.exceptions.ConnectionError):
            success = get_data_from_web('http://www.not_a_real_site.org/')[0]
            self.assertFalse(success)

        success = get_data_from_web('http://www.python.org/blabla')[0]
        self.assertFalse(success)
        success = get_data_from_web('https://www.python.org/dev/peps/')[0]
        self.assertTrue(success)



if __name__ == '__main__':
    unittest.main()
