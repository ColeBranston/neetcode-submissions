class TrieNode():
    def __init__(self):
        self.nei = [None] * 26
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        ref = self.trie

        for c in word:
            index = ord(c) - ord('a')
            if not ref.nei[index]:
                ref.nei[index] = TrieNode()
            ref = ref.nei[index]
        
        ref.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if not node:
                return False

            if i == len(word):
                return node.isEnd

            if word[i] == '.':
                check = False
                for nei in node.nei:
                    check = max(check, dfs(nei, i+1))

                return check 

            index = ord(word[i]) - ord('a')
            
            if not node.nei[index]:
                return False

            return dfs(node.nei[index], i+1)                 

        return dfs(self.trie, 0)
        

