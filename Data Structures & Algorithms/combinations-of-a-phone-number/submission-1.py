class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        mapp = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz',
        }

        output = [""]
        
        '''
        Itterative is quite literally that one backtracking easy where you get all the combinations
        and itteratively add to each added permutation
        '''

        for digit in digits:
            temp = []
            for cur in output:
                for char in mapp[int(digit)]:
                    temp.append(cur + char)

            output = temp
                
        
        return output
        