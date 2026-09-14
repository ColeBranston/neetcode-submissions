class TrieNode():
    def __init__(self):
        self.nei = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.tree = TrieNode()
        
    def insert(self, word: str) -> None:
        ref = self.tree
        for c in word:
            index = ord(c)-ord('a')
            if not ref.nei[index]:
                ref.nei[index] = TrieNode()
            ref = ref.nei[index]

        ref.isEnd = True

    def search(self, word: str) -> bool:
        ref = self.tree
        for c in word:
            index = ord(c)-ord('a')
            if not ref.nei[index]:
                return False

            ref = ref.nei[index]

        return ref.isEnd

    def startsWith(self, prefix: str) -> bool:
        ref = self.tree
        for c in prefix:
            index = ord(c)-ord('a')
            if not ref.nei[index]:
                return False

            ref = ref.nei[index]

        return True
        