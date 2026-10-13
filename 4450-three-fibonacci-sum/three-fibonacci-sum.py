class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        first = 0
        second = 0
        third = 1

        while True:
            #print(first, second, third)
            temp = third
            temp2 = second
            third = second + third
            second = temp
            first = temp2

            if first + second + third >= n:
                break

        return first + second + third == n