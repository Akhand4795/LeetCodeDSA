class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        diff = (sumAlice - sumBob) // 2

        setBob = set(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if b in setBob:
                return [a, b]