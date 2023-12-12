#! /usr/bin/env python3
import unittest
from cosmicpathoptimization import mean_temps


class Test_(unittest.TestCase):

    def test_1(self) -> None:
        """_summary_
        """
        result = mean_temps([10, 2, 38, 23, 38, 23, 21])
        answer = 22
        self.assertEqual(result, answer)

    def test_2(self) -> None:
        """_summary_
        """
        result = mean_temps([11, 60, 45, 5, 2, 22, 19])
        answer = 23
        self.assertEqual(result, answer)

    def test_3(self) -> None:
        """_summary_
        """
        result = mean_temps([1, 1, 1, 1, 1, 1])
        answer = 1
        self.assertEqual(result, answer)

    def test_4(self) -> None:
        """_summary_
        """
        result = mean_temps([43, 45, 76, 45, 65, 50])
        answer = 54
        self.assertEqual(result, answer)

    def test_5(self) -> None:
        """_summary_
        """
        result = mean_temps([100000, 1, 555, 3, 87887])
        answer = 37689
        self.assertEqual(result, answer)

    def test_6(self) -> None:
        """_summary_
        """
        result = mean_temps([34, -2, 32])
        answer = 21
        self.assertEqual(result, answer)
