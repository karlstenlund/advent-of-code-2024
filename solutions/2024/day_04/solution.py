# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from collections import defaultdict
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    @answer(2397)
    def part_1(self) -> int:
        acc = 0
        data: {} = defaultdict(lambda: defaultdict(str))
        for i, row in enumerate(self.input):
            for j, val in enumerate(row):
                data[i][j] = val

        for i in range(len(data)):
            for j in range(len(data[i])):
                horizontal = (
                    data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i][j + 3]
                )
                vertical = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 3][j]
                diagonal_rigth = (
                    data[i][j]
                    + data[i + 1][j + 1]
                    + data[i + 2][j + 2]
                    + data[i + 3][j + 3]
                )
                diagonal_left = (
                    data[i][j]
                    + data[i + 1][j - 1]
                    + data[i + 2][j - 2]
                    + data[i + 3][j - 3]
                )
                words = [horizontal, vertical, diagonal_rigth, diagonal_left]
                acc += words.count("XMAS")
                acc += words.count("SAMX")

        return acc

    # @answer(1234)
    def part_2(self) -> int:
        acc = 0
        data = defaultdict(lambda: defaultdict(str))
        for i, row in enumerate(self.input):
            for j, val in enumerate(row):
                data[i][j] = val

        for i in range(len(data)):
            for j in range(len(data[i])):
                diagonal_rigth = data[i - 1][j - 1] + data[i][j] + data[i + 1][j + 1]
                diagonal_left = data[i - 1][j + 1] + data[i][j] + data[i + 1][j - 1]
                if diagonal_rigth in ["MAS", "SAM"] and diagonal_left in ["MAS", "SAM"]:
                    acc += 1

        return acc

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
