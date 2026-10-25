class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            if i + 2 >= len(arr):
                break

            a, b, c = arr[i], arr[i+1], arr[i+2]
            if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
                return True

        return False