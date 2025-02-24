class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for j in range(len(strs[0])):
            char = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != char:
                    return prefix 
            prefix += char
        
        return prefix
                