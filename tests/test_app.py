from unittest import TestCase
from transform_string.classes import MagicString

class TestUppercase(TestCase):
    def test_uppercase(self):
        actual = MagicString.uppercase("hello world")
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

class TestAlternateCase(TestCase):
    def test_alternatecase(self):
        actual = MagicString.alternatecase("hello world")
        expected = "HeLlO WoRlD"
        self.assertEqual(actual, expected)
