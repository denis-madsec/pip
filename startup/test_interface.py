import unittest
try:
    import config
except ImportError:
    from pathlib import Path
    import os
    import sys
    PROJ_DIR = str(Path(os.path.dirname(os.path.abspath(__file__))).parent)
    sys.path.insert(0, PROJ_DIR)
    import config
from unittest.mock import patch
from startup.interface import get_parsed_list
from startup.get.interface import get_data_or_error


class TestStartupInterface(unittest.TestCase):

    @patch('startup.interface.get_data_or_error')
    def test_persistent_get_parsed_list(self, mocked_get_data_or_error):
        data = '1 title1\n2 title2\n3 title3\n'
        mocked_get_data_or_error.return_value = data, True
        expected_result = [('1', 'title1'),('2','title2'),('3','title3')]
        self.assertEqual(get_parsed_list(), expected_result)


    def test_persistent_get_parsed_list2(self):
        with patch('startup.interface.get_data_or_error') as mocked_get_data:
            data = '1 title1\n2 title2\n3 title3\n'
            mocked_get_data.return_value = data, True
            expected_result = [('1', 'title1'),('2','title2'),('3','title3')]
            self.assertEqual(get_parsed_list(), expected_result)


if __name__ == '__main__':
    unittest.main()
