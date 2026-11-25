class Solution:
    def countValidSubstrings(self, s: str) -> int:
        """
....abc....
     ij

xyzwv
when i=0 j=0, you get x (1 item)
when i=0 j=1, you add y, xy (2 items)
when i=0 j=2, you add z, yz, xyz (3 items)
when i=0 j=3, you add w, zw, yzw X, xyzw X (4 items)
when i=0 j=4, you add v, wv, zwv, yzwv X, xyzwv X (5 items)

Let's say you're trying to avoid everything with yzw in it

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