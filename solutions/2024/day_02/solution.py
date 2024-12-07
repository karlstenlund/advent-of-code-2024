# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    @answer(321)
    def part_1(self) -> int:
        data = [list(map(int, line.split())) for line in self.input]
        acc = 0
        for line in data:
            diff_list = [x[1] - x[0] for x in zip(line, line[1:])]
            if any([x == 0 or x < -3  or x > 3 for x in diff_list]):
                continue
            if all([x > 0 for x in diff_list]):
                acc += 1
                continue
            if all([x < 0 for x in diff_list]):
                acc += 1
                continue
        return acc

    # @answer(1234)
    def part_2(self) -> int:
        data = [list(map(int, line.split())) for line in self.input]
        acc = 0
        for line in data:
            if self.safe_report(line):
                acc += 1

        return acc

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass


    def safe_report(self, line, retry: bool = False):
        diff_list = [x[1] - x[0] for x in zip(line, line[1:])]
        too_big_diff_or_none = [x == 0 or x < -3 or x > 3 for x in diff_list]
        all_positive = [x > 0 for x in diff_list]
        all_negative = [x < 0 for x in diff_list]

        if any(too_big_diff_or_none):
            return self.possible_to_remove_one(line, diff_list) if not retry else False
        if all(all_positive):
            return True
        if all(all_negative):
            return True
        return self.possible_to_remove_one(line, diff_list) if not retry else False

    def possible_to_remove_one(self, line, diff_list):
        wrong_diff = [i for i, x in enumerate(diff_list) if x == 0 or x < -3 or x > 3]
        if len(wrong_diff) == 0:
            wrong_diff = [i for i, x in enumerate(diff_list) if x > 0]
        if len(wrong_diff) > 1:
            wrong_diff = [i for i, x in enumerate(diff_list) if x < 0]
        if len(wrong_diff) != 1:
            return False
        # remove wrong diff
        for i in [max(wrong_diff[0], 0), min(wrong_diff[0] + 1, len(line))]:
            new_line = line.copy()
            # remove element at index i
            new_line.pop(i)
            print(new_line)
            if self.safe_report(new_line, retry=True):
                return True
        return False    


