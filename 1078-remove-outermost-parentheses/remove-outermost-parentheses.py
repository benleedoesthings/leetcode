class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans = []

        for ch in s:
            if ch == "(":
                count += 1
            else:
                count -= 1

            if count == 0 and ch == ")" or count == 1 and ch == "(":
                continue
            else:
                ans.append(ch)

        return "".join(ans)