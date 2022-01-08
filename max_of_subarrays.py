def max_of_subarrays(self,arr,n,k):
        heap = []
        res1 = []
        if k>=n:
            return [max(arr)]
        # curmax = max(arr[:k])
        heappush(heap,(arr[0],0))
        for i in range(len(arr)):
            if i<k-1:
                heappush(heap,(-arr[i],i))
            else:
                heappush(heap,(-arr[i],i))
                while heap and heap[0][1] < (i-k+1):
                    # print('--')
                    heappop(heap)
                max1 = heap[0]
                res1.append(-max1[0])
        return res1
