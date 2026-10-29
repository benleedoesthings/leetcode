class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        a_bits = 0
        b_bits = 0
        while a != 0:
            if a % 2 == 1:
                a_bits += 1
            a = a // 2

        while b != 0:
            if b % 2 == 1:
                b_bits += 1
            b = b // 2

        return a_bits * b_bits if a_bits >= b_bits else b_bits // a_bits