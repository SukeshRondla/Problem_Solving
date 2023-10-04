import math
from typing import List

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = float('inf')

        while l <= r:
            k = (l + r) // 2
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / k)

            if total_hours <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1

        return result
