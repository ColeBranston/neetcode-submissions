class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        for index1, num1 in enumerate(numbers):
            for num2 in numbers[index1:]:
                if (num1 + num2 == target):
                    return [index1 + 1, numbers.index(num2) + 1]
