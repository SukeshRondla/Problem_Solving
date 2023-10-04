def threeSum(nums):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        # Skip duplicates
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            current_sum = a + nums[l] + nums[r]

            if current_sum < 0:
                l += 1
            elif current_sum > 0:
                r -= 1
            else:
                # Found a valid triplet
                res.append([a, nums[l], nums[r]])

                # Skip duplicates
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                # Move pointers
                l += 1
                r -= 1

    return res
