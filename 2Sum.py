from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_indices = {}

        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement] + 1, i + 1]
            num_indices[num] = i

        return []
