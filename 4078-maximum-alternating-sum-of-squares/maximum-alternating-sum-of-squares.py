class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums2 = sorted([num * num for num in nums], reverse=True)
        # in odd length, pick more + than -
        # in even length they're equal
        n = len(nums)
        half = n // 2 if n % 2 == 0 else n // 2 + 1

        pos = nums2[:half]
        neg = nums2[half:]
        #print(pos, neg)

        return sum(pos) - sum(neg)