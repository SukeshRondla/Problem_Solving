class Solution:
    def countBits(self, n: int) -> List[int]:
        sum=0
        list1 = []
        for i in range(n+1):
            sum=bin(i).count("1")
            list1.append(sum)
        return list1