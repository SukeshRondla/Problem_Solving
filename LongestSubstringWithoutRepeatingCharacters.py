
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            lengthStr = r - l + 1
            if lengthStr - maxf > k:
                count[s[l]] -= 1
                l += 1
        return (r - l + 1)


print(Solution().characterReplacement("ABABA",2))