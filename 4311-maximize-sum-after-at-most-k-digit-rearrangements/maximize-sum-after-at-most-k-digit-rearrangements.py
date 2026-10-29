class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:

        total = sum(nums)

        def max_val(num):
            return int(''.join(sorted(str(num), reverse=True)))

        gain = []
        for num in nums:
            gain.append(max_val(num)-num)
        
        gain.sort(reverse=True)
        
        for val in gain[:k]:
                total += val

        return total
        