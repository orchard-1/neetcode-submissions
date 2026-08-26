class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s =[]
        for i in range(len(s)):
            if ord(s[i]) >=65 and ord(s[i]) <=90:
                new_s.append(chr(ord(s[i])+32))
            if ord(s[i]) >=97 and ord(s[i]) <=122:
                new_s.append(s[i])
            if ord(s[i]) >=48 and ord(s[i]) <=57:
                new_s.append(s[i])
                
        j = len(new_s)-1
        for i in range(j+1):
            if new_s[i] != new_s[j]:
                return False
            j-=1
        return True  