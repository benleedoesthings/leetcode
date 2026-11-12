class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1

        inc_streak = 1
        dec_streak = 1

        # inc
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc_streak += 1
                ans = max(ans, inc_streak)
            else:
                inc_streak = 1

            if nums[i - 1] > nums[i]:
                dec_streak += 1
                ans = max(ans, dec_streak)
            else:
                dec_streak = 1

        return ans