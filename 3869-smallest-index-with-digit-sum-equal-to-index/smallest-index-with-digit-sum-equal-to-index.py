class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            temp = num
            dig_sum = 0
            while temp > 0:
                digit = temp % 10
                dig_sum += digit
                temp = temp // 10

            if dig_sum == i:
                return i

        return -1