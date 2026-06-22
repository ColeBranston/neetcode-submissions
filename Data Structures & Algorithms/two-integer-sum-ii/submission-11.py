class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = numbers[0]
        high = numbers[-1]

        middle = numbers[len(numbers) // 2]

        if target < middle:
            high = middle

        elif target > middle:
            low = middle

        else:
            middle = high

        for index1, num1 in enumerate(numbers):
            for num2 in numbers[index1:]:
                if (num1 + num2 == target):
                    return [index1 + 1, numbers.index(num2) + 1]
