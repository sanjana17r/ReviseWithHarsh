def fourSum(self, nums, target):
        # code here
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                left = j+1
                right = len(nums)-1
                while left<right:
                    s = nums[i]+nums[j]+nums[left]+nums[right]
                    if s == target:
                        arr = [nums[i],nums[j],nums[left],nums[right]]
                        arr.sort()
                        res.add(tuple(arr))
                        left+=1
                    elif s> target:
                        right-=1
                    else:
                        left+=1
        res = list(map(list,(list(res))))
        res.sort()
        return res
