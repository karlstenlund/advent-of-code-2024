# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 5

    @answer(7024)
    def part_1(self) -> int:
        orders, updates = self.input.split("\n\n")
        orders = orders.splitlines()
        updates = updates.splitlines()
        order_dict: dict[int, list[int]] = {}
        for order in orders:
            page, after = order.split("|")
            order_dict[int(page)] = order_dict.get(int(page), []) + [int(after)]
        print(order_dict)
        middle_pages = []
        for update in updates:
            correct_order = True
            remaining_pages = [int(page) for page in update.split(",")]
            for page in reversed(update.split(",")):
                pages_after = order_dict.get(int(page), [])
                for page_after in pages_after:
                    if int(page_after) in remaining_pages:
                        print(f"page {page} is not in the correct order")
                        correct_order = False
                        break
                remaining_pages.remove(int(page))
            if not correct_order:
                continue
            pages = update.split(",")
            middle_pages.extend([pages[len(pages) // 2]])

        return sum(int(page) for page in middle_pages)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
