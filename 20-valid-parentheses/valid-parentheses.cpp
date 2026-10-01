class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        unordered_map<char, char> match;
        match[')'] = '(';
        match['}'] = '{';
        match[']'] = '[';

        for (int i = 0; i < s.length(); i++) {
            if (!match.contains(s[i])) {
                st.push(s[i]);
            } else {
                // closer
                if (st.empty()) return false;
                char ch = st.top();
                st.pop();

                if (match[s[i]] != ch) {
                    return false;
                }
            }
        }
        return st.empty();
    }
};