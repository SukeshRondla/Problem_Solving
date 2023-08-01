class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l = i + 1 
            r = len(nums) - 1

            while l < r :
                current_sum = a + nums[l] + nums[r]

                if current_sum < 0:
                    l += 1 
                elif current_sum > 0:
                    r -= 1 
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 

        return res
                
        