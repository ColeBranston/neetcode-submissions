class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            idx = ord(c) - ord('a')

            if cur.children[idx] is None:
                cur.children[idx] = TrieNode()

            cur = cur.children[idx]

        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.word

            c = word[i]

            # Wildcard
            if c == '.':
                for child in node.children:
                    if child and dfs(i + 1, child):
                        return True
                return False

            # Regular character
            idx = ord(c) - ord('a')

            if node.children[idx] is None:
                return False

            return dfs(i + 1, node.children[idx])

        return dfs(0, self.root)