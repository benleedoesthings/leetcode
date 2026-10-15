class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums) + 1):
            print("i=", i)
            j = 0
            k = j + i
            while k <= len(nums):
                print("[" + str(j) + ":" + str(k) + "]")
                dist = len(set(nums[j:k]))
                print("dist=", dist)
                ans += dist * dist
                j += 1
                k = j + i

        return ans