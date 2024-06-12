import unittest
from ft_package.core import count_in_list


class TestCore(unittest.TestCase):
    def test_count_in_list(self):
        self.assertEqual(count_in_list(["toto", "tata", "toto"], "toto"), 2)
        self.assertEqual(count_in_list(["toto", "tata", "toto"], "tutu"), 0)


if __name__ == '__main__':
    unittest.main()
