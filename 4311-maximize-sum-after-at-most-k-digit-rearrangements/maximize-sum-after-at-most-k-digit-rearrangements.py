class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        ten = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
        og_sum = sum(nums)
        
        gains = []
        for num in nums:
            # Optimized digit sorting
            digits = []
            temp = num
            while temp > 0:
                digits.append(temp % 10)
                temp //= 10
            digits.sort()
            
            maxed = sum(digits[i] * ten[i] for i in range(len(digits)))
            gain = maxed - num
            if gain > 0:
                gains.append(gain)
                
        # Sort descending and take the top k positive gains
        gains.sort(reverse=True)
        return og_sum + sum(gains[:k])