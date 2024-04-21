class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def helper(number, length, n, k):
            if length == n:
                res.append(number)
                return
            if length > n: return
            last = number % 10
            a = last + k
            b = last - k
            if not (b < 0) and k != 0:
                d = number * 10 + b
                helper(d, length+1, n, k)
            if not (a >= 10):
                c = number * 10 + a
                helper(c, length+1, n, k)
        for i in range(1, 10): helper(i, 1, n, k)
        return res