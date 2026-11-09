class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                waiting_day = stack.pop()
                result[waiting_day] = index - waiting_day

            stack.append(index)

        return result
            