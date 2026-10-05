class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0

        freq = defaultdict(int)
        maj_char = None
        maj = 0
        other = 0

        ans = 0

        """
CBBBA k=1

maj  : B
other: 1

want:
CBBB
BBBA

AAABABB
maj  : B
other: 1

AAABBBB
maj_char: A
maj: 1
other: 2
        """

        while i <= j and j < len(s):
            #print("curr", s[j])
            freq[s[j]] += 1
            if freq[s[j]] > maj:
                maj_char = s[j]
                maj = freq[s[j]]

            if s[j] != maj_char:
                other += 1

            while other > k:
                if maj < other:
                    # that is no longer the majority character, recount
                    #print("recounting")
                    #print(freq)
                    maj, maj_char = sorted([(count, ch) for ch, count in freq.items()], reverse=True)[0]
                    #print(i, j)
                    other = (j - i + 1) - maj
                    #print(maj, maj_char, other)
                    #break

                if not (other > k):
                    break

                if s[i] == maj_char:
                    maj -= 1
                else:
                    other -= 1

                freq[s[i]] -= 1

                i += 1

            #print("maj", maj_char, " other", other)
            #print("i=", i, " j=", j)
            #print(i <= j)

            ans = max(ans, j - i + 1)
            j += 1

        return ans