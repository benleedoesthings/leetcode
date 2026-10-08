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
                #print("END")

            elif not fragment_started:
                #print("BEGIN")
                fragment_started = True
            else:
                ans.append(ch)

            #print(count)

        return "".join(ans)