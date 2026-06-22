class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(numbers):
            for index2, num2 in enumerate(numbers):
                if num1 + num2 == target:
                    return [index1 + 1, index2 + 1]

