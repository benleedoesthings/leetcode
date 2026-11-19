class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        def is_consistent(nums):
            x = nums[0]
            min_val = nums[0]
            for i in range(1, len(nums)):
                x = x & nums[i]
                min_val = min(min_val, nums[i])

            return x == min_val

        count = 0

        for i in range(1, len(nums) + 1):
            for j in range(len(nums) - i + 1):
                if is_consistent(nums[j:j+i]):
                    count += 1

        return count