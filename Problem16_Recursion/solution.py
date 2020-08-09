from typing import List


class Solution:
    lookup = {"2": "abc",
              "3": "def",
              "4": "ghi",
              "5": "jkl",
              "6": "mno",
              "7": "pqrs",
              "8": "tuv",
              "9": "wxyz"}

    def __init__(self):
        self.solutions = []

    def solve(self, ip: str, op: str):
        if not ip:
            self.solutions.append(op)
            return

        digit_to_process = ip[0]
        next_ip = ip[1:] if len(ip) > 1 else ""
        for char_to_process in Solution.lookup[digit_to_process]:
            self.solve(next_ip, op + char_to_process)

    def letter_combinations(self, digits: str) -> List[str]:
        if digits:
            self.solve(digits, "")
        return self.solutions
