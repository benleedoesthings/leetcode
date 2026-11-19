class Solution:
    def trap(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1

        max_left = 0
        max_right = 0

        ans = 0
        while i < j and j < len(height):
            max_left = max(max_left, height[i])
            max_right = max(max_right, height[j])

            if height[i] < max_left:
                ans += max_left - height[i]

            if height[j] < max_right:
                ans += max_right - height[j]

            if max_left < max_right:
                i += 1
            else:
                j -= 1

        return ans