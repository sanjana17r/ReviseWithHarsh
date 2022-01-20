def subArraySum(self,nums, n, k): 
       #Write your code here
        count = 0
        sums = 0
        d = dict()
        d[0]=-1
        for i in range(len(nums)):
            sums += nums[i]
            d[sums] = i
            if sums-k in d:
                h = d[sums-k]
                return [h+2,i+1]
        return [-1]
