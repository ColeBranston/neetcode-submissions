class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        if not digits:
            return []

        output = [""]


        for num in digits:
            temp = []
            for curr in output:
                for letter in mapp[int(num)]:
                    temp.append(curr + letter)

            output = temp

        return output
            
