class Solution:
    def countValidSubstrings(self, s: str) -> int:
        """
....abc....
     ij

xyabcd
   i j
i=0 j=0 add x
i=0 j=1 add y, xy
i=0 j=2 add a, ya, xya
i=0 j=3 add b, ab, yab, xyab
i=3 j=4 add c, bc
i=3 j=5 add d, cd, bcd
        """

        i = 0
        j = 0
        valid = 0
        while i <= j and j < len(s):
            if j >= 2 and s[j-2] == "a" and s[j-1] == "b" and s[j] == "c":
                # abc found
                i = j - 1

            valid += j - i + 1

            j += 1

        return valid