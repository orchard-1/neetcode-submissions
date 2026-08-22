class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hash:
                return [hash[val],i]
            else:
                hash[nums[i]] =i