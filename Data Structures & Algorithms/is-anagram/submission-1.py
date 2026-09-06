class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS,mapT ={},{}
        if len(s) != len(t):
            return False
        else:
            for char in s:
                mapS[char] = mapS.get(char,0)+1
            for char in t:
                mapT[char] = mapT.get(char,0)+1
            
            for key in mapT:
                if mapT[key] != mapS.get(key,0):
                    return False
            return True
                
        