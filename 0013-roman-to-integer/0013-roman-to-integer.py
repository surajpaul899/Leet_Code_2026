class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value = [1, 5, 10, 50, 100, 500, 1000]
        dict1 = dict(zip(Roman, value))
        sum = 0
        if len(s)==0:
            return 0
        elif len(s)==1:
            return dict1[s[0]]
        else:
            for i in range(len(s)-1):
                 if dict1[s[i]]<dict1[s[i+1]]:
                  sum-=dict1[s[i]]
                 else:
                  sum+=dict1[s[i]]
        sum+=dict1[s[-1]]     
        return sum