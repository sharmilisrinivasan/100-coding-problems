from typing import List


class Solution:
    def __init__(self):
        self.solutions = []

    def solve(self, candidates, sum_req, op):
        if sum_req == 0:
            self.solutions.append(op)
            return

        if not candidates:
            return

        for idx, candidate in enumerate(candidates):
            if candidate <= sum_req:
                self.solve(candidates[idx:], sum_req - candidate, op + [candidate])
            else:
                break

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.solve(candidates, target, [])
        return self.solutions
