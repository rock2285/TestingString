import unittest

class TestStringMethod_Upper(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO', "'foo'.upper()=='FOO'")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper(),"isupper positive case")
        self.assertFalse('Foo'.isupper(), "isupper negative case")

class TestStringMethod_Split(unittest.TestCase):
    def test_twoWords(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'], "split on a space")

    def test_splitInt(self):
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError, "invalid separator"):
            s = 'hello world'
            s.split(2)