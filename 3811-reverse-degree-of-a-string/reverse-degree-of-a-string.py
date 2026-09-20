class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum([(26 - (ord(ch) - 97)) * (i+1) for i, ch in enumerate(s)])