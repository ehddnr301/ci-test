import unittest
import main


class MainTest(unittest.TestCase):
    def test_hello_world(self):
        ret = main.hello_world("test")
        self.assertEqual(ret, "test1")


if __name__ == "__main__":
    unittest.main()
