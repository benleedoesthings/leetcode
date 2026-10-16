class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sd = 0
        dd = 0
        for num in nums:
            if num < 10:
                sd += num
            else:
                dd += num

        return sd != dd