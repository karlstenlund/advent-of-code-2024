# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer
from ...utils.list import parse_input_2_column_list


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(936063)
    def part_1(self) -> int:
        list_1, list_2 = parse_input_2_column_list(self.input)
        sorted_list_1 = sorted(list_1)
        sorted_list_2 = sorted(list_2)
        acc =  0
        for i in range(len(sorted_list_1)):
            acc += abs(sorted_list_1[i] - sorted_list_2[i])

        return acc



    @answer(23150395)
    def part_2(self) -> int:
        list_1, list_2 = parse_input_2_column_list(self.input)
        # make list_2 a dict for faster lookup with numerb of occurences in list_2
        list_2_dict = {i: 0 for i in list_2}
        for i in list_2:
            list_2_dict[i] += 1
        
        # count occurences of numbers in list_1 that are in list_2
        acc = 0
        for i in list_1:
            if i in list_2_dict:
                acc += list_2_dict[i] * i
        return acc



