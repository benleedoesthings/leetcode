class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1

        streak = 1

        # inc
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                streak += 1
                ans = max(ans, streak)
            else:
                streak = 1
        
        streak = 1

        # dec
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                streak += 1
                ans = max(ans, streak)
            else:
                streak = 1

        return ans