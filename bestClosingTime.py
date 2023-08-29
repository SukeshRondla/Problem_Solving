class Solution:
    def bestClosingTime(self, customers: str) -> int:
        result = 0
        balance = 0
        
        for i in range(len(customers)):
            if customers[i] == 'N':
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    result = i + 1
                    balance = 0
        
        return result

