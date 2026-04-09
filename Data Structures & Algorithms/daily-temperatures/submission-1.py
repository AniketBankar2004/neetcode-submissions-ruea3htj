class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = [] #temp, idx pair

        for idx,num in enumerate(temperatures):
            while stack and num > stack[-1][0]:
                stack_num , stack_idx = stack.pop()
                result[stack_idx ] = (idx - stack_idx)
            stack.append([num,idx])
        return result


        