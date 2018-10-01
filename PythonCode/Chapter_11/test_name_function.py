import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """
    Test name_function.py
    """

    def test_first_last_name(self):
        """
        Dose the founction can deal with names like Janis Joplin?
        """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """
        Dose the founction can deal with names like Sheldon Lee Cooper?
        """
        formatted_name = get_formatted_name('sheldon', 'cooper' ,'lee')
        self.assertEqual(formatted_name, 'Sheldon Lee Cooper')

unittest.main()
