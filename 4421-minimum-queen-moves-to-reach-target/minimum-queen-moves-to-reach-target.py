class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if source == target:
            return 0

        row_diff = abs(target[0] - source[0])
        col_diff = abs(target[1] - source[1])

        if row_diff == col_diff:
            return 1

        if source[0] == target[0] or source[1] == target[1]:
            return 1

        # You can always go row and then col
        return 2