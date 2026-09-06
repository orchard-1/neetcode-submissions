class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansMap ={}
        for word in strs:
            charMap =[0]*26
            for char in word:
                charMap[ord(char)-97]+=1
            strMap = []
            for i in range(26):
                if charMap[i] > 0:
                    strMap.append(chr(i+97)+str(charMap[i]))
            if ("".join(strMap)) in ansMap:
                ansMap["".join(strMap)].append(word)
            else:
                ansMap["".join(strMap)] = [word]
        ans = []
        for key,value in ansMap.items():
            ans.append(value)
        return ans
        