import unittest
from faker import Faker, Generator
import faker_representation


class RepresentationProviderTestCase(unittest.TestCase):
    """Provider test case."""

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(faker_representation.Provider)

    def test_lists_in_order(self):
        """Test interal values are in order."""
        for attr_name, attr in faker_representation.__dict__.items():
            with self.subTest(attr_name=attr_name):
                if isinstance(attr, list):
                    self.assert_list_in_order(attr)

    def assert_list_in_order(self, the_list):
        """Assert a list is in order."""
        prev_value = ""
        for this_value in the_list:
            self.assertGreaterEqual(this_value, prev_value)
            prev_value = this_value

    def test_no_duplicates(self):
        """Test value lists don't contain duplicates."""
        for attr_name, attr in faker_representation.__dict__.items():
            with self.subTest(attr_name=attr_name):
                if isinstance(attr, list):
                    self.assertEqual(len(attr), len(set(attr)))

    def test_nonbinary_name(self):
        """Test that generated institution name is at least one word long."""
        result = self.fake.nonbinary_name()
        word_count = len(result.split())
        self.assertGreaterEqual(word_count, 1)
    
    def test_diverse_first_name(self):
        """Test that generated institution name is at least one word long."""
        result = self.fake.diverse_first_name()
        word_count = len(result.split())
        self.assertGreaterEqual(word_count, 1)

if __name__ == "__main__":
    unittest.main()
