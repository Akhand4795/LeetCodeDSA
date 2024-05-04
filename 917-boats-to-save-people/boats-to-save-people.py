class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        result = 0
        people.sort(reverse=True)
        while l <= r:
            if people[l] <= limit: 
                if people[l] < limit:
                    if people[l] + people[r] <= limit:
                        result += 1
                        l += 1
                        r -= 1
                    else:
                        result += 1
                        l += 1
                else:
                    result += 1
                    l += 1
        return result