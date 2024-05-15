class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Step 1: Calculate the GCD of a and b
        gcd_ab = math.gcd(a, b)
        
        # Step 2: Count the factors of the GCD
        count = 0
        for i in range(1, gcd_ab + 1):
            if gcd_ab % i == 0:
                count += 1
                
        return count