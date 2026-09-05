class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word=strs[0]
        for i in range (len(strs)):
            if (len(strs[i])<len(min_word)):
                min_word=strs[i]
        common=[]
        blank=""
        for j in range (len(min_word)):
            for i in range(len(strs)):
                if (min_word[j]!=strs[i][j]):
                    return "".join(common)
            common.append(min_word[j])
                
        return "".join(common)
