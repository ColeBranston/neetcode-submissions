class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t):
            stor1 = {}
            stor2 = {}

            for char in s:
                if char not in stor1:
                    stor1[char] = 1

                else:
                    stor1[char] += 1

            for char in t:
                if char not in stor2:
                    stor2[char] = 1

                else:
                    stor2[char] += 1

            for char in s:
                if char in stor1 and char in stor2:
                    if stor1[char] == stor2[char]:
                        pass

                    else:
                        return False

                else:
                    return False

            for char in t:
                if char in stor1 and char in stor2:
                    if stor1[char] == stor2[char]:
                        pass

                    else:
                        return False

                else:
                    return False

            return True

        tempStor = {}

        for word in strs:
            bool = True
            for key in list(tempStor.keys()):
                if isAnagram(word, key):
                    tempStor[key].append(word)
                    bool = False
                    break

            if bool:
                tempStor[word] = [word]

        returnValue = [(subArray) for subArray in list(tempStor.values())]

        return returnValue