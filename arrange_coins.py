
"""
    Arranging Coins (Mathematical Approach)

    This solution finds the maximum number of complete staircase rows 
    that can be formed using `n` coins.

    Instead of using loops, we apply the mathematical formula 
    for the sum of first `k` natural numbers:

        k(k + 1) / 2 ≤ n

    Solving the quadratic equation:

        k^2 + k - 2n = 0

    Using quadratic formula:

        k = ⌊(-1 + √(1 + 8n)) / 2⌋

    This allows us to compute the result in O(1) time complexity 
    and O(1) space complexity, making it highly efficient 
    for large inputs.
    """

import math

class Stair_case:
    def arrangeCoins(self, n):
        return int((math.sqrt(1 + 8*n) - 1) // 2)
    

n=int(input())
result=Stair_case()
print(result.arrangeCoins(n))