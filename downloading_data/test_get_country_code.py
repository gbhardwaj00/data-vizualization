import unittest
from country_codes import get_country_code


class CountryCodeTestCase(unittest.TestCase):
    """Test case for the get_country_code function.
    """

    def test_correct_country_code(self):
        """Test that the correct country code is returned for a given country name."""
        self.assertEqual(get_country_code('United States'), 'us')
        self.assertEqual(get_country_code('Canada'), 'ca')
        self.assertEqual(get_country_code('Mexico'), 'mx')

    def test_country_not_found(self):
        """Test that None is returned for a country name not found in the data."""
        self.assertIsNone(get_country_code('Atlantis'))
        self.assertIsNone(get_country_code('Narnia'))
        self.assertIsNone(get_country_code('Middle Earth'))

    def test_country_with_different_name(self):
        """Test that the correct country code is returned for a country with a different name in the data."""
        self.assertEqual(get_country_code('Bolivia'), 'bo')
        self.assertEqual(get_country_code('Congo, Dem. Rep.'), 'cd')
        self.assertEqual(get_country_code('Egypt, Arab Rep.'), 'eg')

    def test_case_insensitive(self):
        """Test that the function is case-insensitive."""
        self.assertIsNone(get_country_code('united states'), 'us')
        self.assertIsNone(get_country_code('CANADA'), 'ca')
        self.assertIsNone(get_country_code('mExIcO'), 'mx')

if __name__ == '__main__':
    unittest.main()