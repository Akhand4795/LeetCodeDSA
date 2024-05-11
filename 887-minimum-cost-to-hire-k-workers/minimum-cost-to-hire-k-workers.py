from heapq import *
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        lst = []
        for i in range(len(wage)):
            lst.append((wage[i] / quality[i], quality[i]))
        lst.sort()
        quality_sum = 0
        min_cost = float('inf')
        heap = []
        for ratio, qual in lst : 
            heappush(heap, -qual)
            quality_sum += qual

            if(len(heap) > k):
                quality_sum += heappop(heap)
            if(len(heap) == k):
                min_cost = min(min_cost, ratio * quality_sum)
        return min_cost