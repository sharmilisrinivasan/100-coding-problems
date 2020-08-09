from typing import List


class Solution:

    def solve(self, board: List[List[str]], word: str,
              row: int, col: int, word_pos: int, visited: set):

        # False cases
        # Visited check + Criteria check
        if ((row, col) in visited) or board[row][col] != word[word_pos]:
            return False

        # Base case
        if word_pos + 1 == len(word):
            return True

        # Proceed Further on criteria pass

        # Progress right
        if ((col + 1) < len(board[row]) and
                self.solve(board, word, row, col + 1, word_pos + 1, visited.union({(row, col)}))):
            return True

        # Progress down
        if ((row + 1) < len(board) and
                self.solve(board, word, row + 1, col, word_pos + 1, visited.union({(row, col)}))):
            return True

        # Progress left
        if ((col - 1) >= 0 and
                self.solve(board, word, row, col - 1, word_pos + 1, visited.union({(row, col)}))):
            return True

        # Progress up
        if ((row - 1) >= 0 and
                self.solve(board, word, row - 1, col, word_pos + 1, visited.union({(row, col)}))):
            return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            col_size = len(board[row])
            for col in range(col_size):
                if board[row][col] == word[0]:
                    if self.solve(board, word, row, col, 0, set()):
                        return True
        return False
