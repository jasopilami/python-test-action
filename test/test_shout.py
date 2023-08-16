import unittest
from shout import shout


class TestShout(unittest.TestCase):
    def test_shout_uppercase(self):
        got = shout("hello, world!")
        want = "HELLO, WORLD!"

        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
