from typing import List


class Solution:
    def __init__(self):
        self.solutions = []

    def solve(self, in_str: str, op: List[str]):

        if not in_str:
            self.solutions.append(op)
            return

        for idx in range(len(in_str)):
            word1 = in_str[:(idx + 1)]
            word2 = in_str[(idx + 1):]

            # is_palindrome
            if word1 == word1[::-1]:
                self.solve(word2, op + [word1])

    def partition(self, s: str) -> List[List[str]]:
        self.solve(s, [])
        return self.solutions
