# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import TextSolution, answer 
import re


class Solution(TextSolution):
    _year = 2024
    _day = 3

    @answer(160672468)
    def part_1(self) -> int:
        regex = r"mul\((\d+),(\d+)\)"
        matches = re.findall(regex, self.input)
        if matches:
            return sum(int(a) * int(b) for a, b in (map(int, match) for match in matches))
        return 0

    @answer(84893551)
    def part_2(self) -> int:
        # Match for 'mul(a,b), don't() or do()
        regex = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
        matches = re.finditer(regex, self.input)
        enabled = True
        acc = 0
        print(matches)
        for match in matches:
            if match.group(0) == "do()":
                enabled = True
            elif match.group(0) == "don't()":
                enabled = False
            elif enabled and match.group(0).startswith("mul"):
                a, b = map(int, match.groups())
                acc += a * b
        return acc
