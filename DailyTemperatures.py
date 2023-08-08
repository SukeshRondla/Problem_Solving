from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day
        stack.append(i)

    return answer


print(dailyTemperatures([2,2,2,3]))
