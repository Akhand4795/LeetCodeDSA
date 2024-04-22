class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}
        
        def dfs(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]
            
            cost = sum(needs[i] * price[i] for i in range(len(needs)))
            
            for offer in special:
                clone = needs[:]
                for i in range(len(needs)):
                    if clone[i] < offer[i]:
                        break
                    clone[i] -= offer[i]
                else:
                    cost = min(cost, offer[-1] + dfs(clone))
            
            memo[tuple(needs)] = cost
            return cost
        
        return dfs(needs)