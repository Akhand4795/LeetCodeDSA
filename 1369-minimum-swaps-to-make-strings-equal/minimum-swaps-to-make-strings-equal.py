class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count_xy = count_yx = 0
    
        for c1, c2 in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                count_xy += 1
            elif c1 == 'y' and c2 == 'x':
                count_yx += 1
        
        if (count_xy + count_yx) % 2 != 0:
            return -1
        
        return (count_xy + 1) // 2 + (count_yx + 1) // 2