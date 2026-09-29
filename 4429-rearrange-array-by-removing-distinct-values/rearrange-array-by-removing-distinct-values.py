class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while nums:
            num_set = sorted(set(nums))
            for num in num_set:
                ans.append(num)
                nums.remove(num)

        return ans