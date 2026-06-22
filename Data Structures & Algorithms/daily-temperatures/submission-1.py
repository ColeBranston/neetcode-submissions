class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # given an array of temperatures where the location in the array is on the ith day
        # want to return an array where each element is the number of days after the ith day before
            # a warmer temparature appears on a future day. No number of days after that will be warmer
            # input 0 for that ith position

        #### Brute Force O(n^2) ####

        # def calcDays(array):
        #     counter = 0
        #     initial = array[0]

        #     for temp in array:
        #         if temp > initial:
        #             return counter

        #         else:
        #             counter += 1

        #     return 0

        # res = []
        # for i in range(len(temperatures)):
        #     res.append(calcDays(temperatures[i:]))

        # return res
        
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res


        
        

        
        