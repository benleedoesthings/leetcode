class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq = defaultdict(int)
        max_freq = 0
        for num in nums:
            freq[num] += 1
            max_freq = max(freq[num], max_freq)

        groups = [[] for _ in range(max_freq)]

        for num, count in sorted(freq.items()):
            for i in range(count):
                groups[i].append(num)

        ans = []
        for arr in groups:
            for num in arr:
                ans.append(num)

        return ans