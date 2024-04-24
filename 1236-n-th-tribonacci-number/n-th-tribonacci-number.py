class Solution:
    def tribonacci(self, n: int) -> int:
        sum = 0
        t1, t2, t3 = 0, 1, 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n == 3:
            return 2
        for i in range(2, n):
            sum = t1 + t2 + t3
            t1, t2, t3 = t2, t3, sum
        return t3

        