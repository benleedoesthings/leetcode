class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        """
        groups = []
        groups.append([nums[0], 1])
        for i in range(1, len(nums)):
            if groups[-1][0] == nums[i]:
                groups[-1][1] += 1
            else:
                groups.append([nums[i], 1])

        print(groups)
        """
        freq = defaultdict(int)
        total_curr_pairs = 0
        max_unequal_pair_count = 0

        for i in range(len(nums) - 1):
            j = i + 1
            pair = (nums[i], nums[j]) if nums[i] < nums[j] else (nums[j], nums[i])
            if nums[i] == nums[j]:
                total_curr_pairs += 1
            else:
                freq[pair] += 1
            max_unequal_pair_count = max(max_unequal_pair_count, freq[pair])
        
        #print(freq, total_curr_pairs)

        return max_unequal_pair_count + total_curr_pairs