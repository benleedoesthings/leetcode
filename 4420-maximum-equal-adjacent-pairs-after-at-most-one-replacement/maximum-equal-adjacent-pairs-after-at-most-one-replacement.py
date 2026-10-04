class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
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

        return max_unequal_pair_count + total_curr_pairs