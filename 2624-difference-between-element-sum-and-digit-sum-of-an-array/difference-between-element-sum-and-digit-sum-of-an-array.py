class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        def digit_sum(num):
            ret = 0
            while num != 0:
                ret += num % 10
                num = num // 10

            return ret

        return abs(sum(nums) - sum([digit_sum(num) for num in nums]))