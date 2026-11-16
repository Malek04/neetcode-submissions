class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        t1 = sorted(t)
        s1 = sorted(s)

        return t1 == s1