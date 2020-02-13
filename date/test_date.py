import unittest
from date import Date


class MyTestCase(unittest.TestCase):

    def test_numb_value(self):
        self.assertRaises(ValueError, Date, 20, 12)

    def test_value(self):
        date_ = Date(2020, 12, 23)
        self.assertEqual(date_.date, '23.12.2020')

    def test_is_leap_year(self):
        date_ = Date(2020, 2, 29)
        self.assertTrue(date_.is_leap_year(2020))

    def test_add_year(self):
        date_ = Date(2020, 2, 29)
        date_.add_year(1)
        self.assertEqual(date_.date, '1.3.2021')

    def test_wrong_add_year(self):
        date_ = Date(2020, 2, 29)
        self.assertRaises(TypeError, date_.add_day, 'sdfa')


if __name__ == '__main__':
    unittest.main()
