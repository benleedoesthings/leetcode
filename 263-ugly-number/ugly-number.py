class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        def prime(n):
            #print("checking prime for", n)
            if n < 2:
                #print("not")
                return False

            for i in range(2, math.floor(math.sqrt(n)) + 1):
                #print("check div by", i, "or", n//i)
                if n % i == 0 or n % (n//i) == 0:
                    #print("not")
                    return False

            #print('is')
            return True

        for i in range(1, math.floor(math.sqrt(n)) + 1):
            #print("main: checking factors", i, n//i)
            if (prime(i) and n % i == 0 and i > 5) or (prime(n // i) and n % (n//i) == 0 and n // i > 5):
                #print("Factor:", i, "or", n // i)
                return False

        return True