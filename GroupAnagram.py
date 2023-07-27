class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        a = 0
        b = len(s)-1
        s.replace(" ", "")


        while True:

            if s[a] == s[b]:
             a += 1
             b -= 1
            elif a == b:
                break

            else:
                return False


        return True


i = Solution()
