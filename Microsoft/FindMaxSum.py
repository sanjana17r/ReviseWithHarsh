def FindMaxSum(self,nums, n):
        if len(nums)<=2:
            return max(nums)
        nums[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            #value = nums[i]
            nums[i] = max(nums[i-1],nums[i-2]+ nums[i])
        return nums[-1]
