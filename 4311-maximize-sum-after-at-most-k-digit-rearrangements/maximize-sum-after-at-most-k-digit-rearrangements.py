class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        """
1 digit = useless
2 digit -> 34 -> 43 greater number 1st smaller 2nd
30 -> can't do anything

3 digit -> 157 -> 751
107 -> 170

        """
        ten = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

        def max_out(num):
            digits = []
            temp = num
            while temp != 0:
                digits.append(temp % 10)
                temp = temp // 10

            digits.sort()
            
            res = 0
            for i in range(len(digits)):
                res += digits[i] * ten[i]

            return res

        # Find the maximum GAINZZZ
        num_gain = [0] * len(nums)
        for i, num in enumerate(nums):
            maxed = max_out(num)
            gain = maxed - num
            num_gain[i] = [-gain, i]

        heapq.heapify(num_gain)
        #print(num_gain)

        for i in range(k):
            gain, index = heapq.heappop(num_gain)
            #print(gain, index)
            nums[i] -= gain

        return sum(nums)