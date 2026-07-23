class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False
        st=set(s)
        dict1={}
        for i in range(len(s)):
            dict1[s[i]]=dict1.get(s[i], 0)+1
        for i in range(len(t)):
            dict1[t[i]]=dict1.get(t[i], 0)-1
        for val in dict1.values():
            if val != 0:
                return False
        return True