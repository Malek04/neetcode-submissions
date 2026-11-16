class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        s1 = s.lower()
        for c in s1:
            if(c>='a' and c<='z' or c>='0' and c<='9'):
                new += c
        return new == new[::-1]