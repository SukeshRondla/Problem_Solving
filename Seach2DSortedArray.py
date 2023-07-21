class Solution(object):
    def searchMatrix(self, matrix, target):

        for lis in matrix:

            p1 = 0
            p2 = len(lis) - 1

            while (p1 <= p2):

                mid = (p1 + p2) / 2

                if lis[mid] == target:
                    return True

                if target > lis[mid]:
                    p1 = mid + 1
                else:
                    p2 = mid - 1

        return False

