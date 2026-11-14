class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for size in range(l, r+1):
            i = 0
            j = 0
            total = 0
            # Add initially
            for _ in range(size):
                total += nums[j]
                j += 1

            if total > 0:
                ans = min(ans, total)

            while j < len(nums):
                total += nums[j]
                j += 1

                total -= nums[i]
                i += 1

                if total > 0:
                    ans = min(ans, total)

        return -1 if ans == float('inf') else ans