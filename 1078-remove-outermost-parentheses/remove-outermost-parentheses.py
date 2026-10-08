class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        fragment_started = False
        ans = []

        for ch in s:
            if ch == "(":
                count += 1
            else:
                count -= 1

            if fragment_started and count == 0:
                fragment_started = False
            elif not fragment_started:
                fragment_started = True
            else:
                ans.append(ch)

        return "".join(ans)