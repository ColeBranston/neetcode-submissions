class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [['dummy']]

        for i in range(len(strs)):
            print("Currently on: ", strs[i])
            flag = False
            for j in range(len(res)):
                if Counter(strs[i]) == Counter(res[j][0]):
                    res[j].append(strs[i])
                    flag = True

            if not flag:
                res.append([strs[i]])

        return res[1:]