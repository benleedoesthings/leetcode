class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False
        for ch in s:
            if seen_b and ch == "a":
                return False

            if ch == "b":
                seen_b = True
        return True

        """

"aaabbb"

abab
ij

goal: find first b
see a -> everything before it and it is a, so left = mid + 1
see b -> everything after it is b, right = mid

        """
        left = 0
        right = len(s) - 1
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            if s[mid] == "a":
                left = mid + 1
            else:
                right = mid

        print(left)
        
        return False