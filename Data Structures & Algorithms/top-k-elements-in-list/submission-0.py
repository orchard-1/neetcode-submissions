class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}
        for num in nums:
            if num in map:
                map[num]+=1
            else:
                map[num]=1

        ans =[]
        maxEle = 0
        maxVal = 0
        for i in range(k):
            maxVal = 0
            for key, value in map.items():
                if value  > maxVal:
                    maxEle = key
                maxVal = max(value,maxVal)
            ans.append(maxEle)
            map[maxEle]=0
        return ans    