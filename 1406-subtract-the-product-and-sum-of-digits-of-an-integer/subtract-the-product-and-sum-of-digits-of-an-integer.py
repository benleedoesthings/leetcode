class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        su = 0
        while n != 0:
            d = n % 10
            prod *= d
            su += d
            n = n // 10

        return prod - su