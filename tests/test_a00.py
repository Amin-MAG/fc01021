import unittest

from a00.q01_hello_friend import say_hello
from a00.q02_calculate_sum import calculate_sum
from a00.q03_count_strings import count_strings


class TestA01(unittest.TestCase):

    def test_hello_friend(self):
        test_cases = (
            ("Eliot", "Hello Eliot!"),
            ("Bob", "Hello Bob!"),
            ("Woooo oooo rrr llld :))", "Hello Woooo oooo rrr llld :))!"),
            (":)=<", "Hello :)=<!"),
            ("Black R05e", "Hello Black R05e!"),
        )

        for tc in test_cases:
            tc_input, tc_output = tc
            self.assertEqual(say_hello(tc_input), tc_output)


    def test_calculate_sum(self):
        test_cases = (
            ((1, 2, 3), 6),
            ((0, 2, 3), 5),
            ((1, 2, 3, 3, 3, 3), 15),
            ((1, 2, 2**10), 1027),
            ((832, -32, 3), 803),
            ((-1, -20, 3), -18),
        )

        for tc in test_cases:
            numbers, answer = tc
            self.assertEqual(calculate_sum(numbers), answer)

    def test_count_strings(self):
        test_cases = (
            ((23, "212", 23, 12), 1),
            (("Helllo", None, "212", 23, 12), 2),
            ((23, b"23333322", "eX01020030", -231), 0),
            (("programming", "linux", "ComputerRRRSS"), 3),
        )

        for tc in test_cases:
            ls, count = tc
            self.assertEqual(count_strings(ls), count)

if __name__ == '__main__':
    unittest.main()
