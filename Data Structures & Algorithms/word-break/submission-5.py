class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Approach is to check at the index if any of the words could start there, involving three main checks
            1. that the current index i + length of word in wordDict is less than the length of the string,
            that way the dfs traversal doesn't go over the string size
            2. checks that from the current index until the length of the word + i offset from current index
            is == to the word we are checking against
            3. final check to see if the future words in wordDict can be broken from the s with dfs(i + len(w)),
            where len(w) is the length of the current word

        If none of these conditions are met for any of the words in the wordDict, then we memoize the result 
        at the current index, and return False, therefore propogating back to the intial call and returning
        False in that scenario
        '''
        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]

            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                     s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)