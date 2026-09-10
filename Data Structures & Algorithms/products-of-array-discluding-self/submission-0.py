class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lSum =[1]*len(nums)
        rSum =[1]*len(nums)

        for i in range(1,len(nums)):
            lSum[i] = nums[i-1]*lSum[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            rSum[j] = nums[j+1] * rSum[j+1]

        for i in range(len(lSum)):
            lSum[i]*=rSum[i]
        return lSum