class Solution {
public:
    char openers[3] = { '(', '{', '[' };
    char closers[3] = { ')', '}', ']' };

    int openerPos(char opener) {
        for (int i = 0; i < size(openers); i++) {
            if (opener == openers[i]) {
                return i;       
            }
        }
        return -1;
    }

    int closerPos(char closer) {
        for (int i = 0; i < size(closers); i++) {
            if (closer == closers[i]) {
                return i;       
            }
        }
        return -1;
    }

    bool isMatch(char opener, char closer) {
        int openerIdx = openerPos(opener);
        int closerIdx = closerPos(closer);

        // should never happen
        if (openerIdx == -1 || closerIdx == -1) {
            return false;
        }

        return openerIdx == closerIdx;
    }

    bool isValid(string s) {
        stack<int> st;

        for (int i = 0; i < s.length(); i++) {
            if (openerPos(s[i]) != -1) {
                st.push(s[i]);
            } else {
                if (st.empty()) return false;
                char ch = st.top();
                st.pop();
                if (!isMatch(ch, s[i])) {
                    return false;
                }
            }
        }
        return st.empty();
    }
};