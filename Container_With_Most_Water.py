class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0 
        max_r = max(height)

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1 
            else :
                r -= 1 

            if (r - l) * max_r <= res:
                break

        return res