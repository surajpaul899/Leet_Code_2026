class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) ==0:
            return ""
        
        elif len(strs)==1:
                return strs[0]
        else:
            for i in range(len(strs[0])):
                for string in strs[1:]:
                    if i>=len(string) or string[i]!=strs[0][i]:
                        return strs[0][:i]
            return strs[0]
        
        