def longestMountain(self, arr: List[int]) -> int:
        flag = 0
        i=1
        count,cur = 0,1
        while i<len(arr):
            while i<len(arr) and arr[i]>arr[i-1]:
                cur+=1
                if flag == 0:
                    flag = 1
                    cur = 2
                if flag == 2:
                    cur = 2
                    flag = 1
                    count = max(count,cur)
                i+=1
            if i<len(arr) and arr[i] == arr[i-1]:
                i+=1
                flag = 0
            while i<len(arr) and arr[i]<arr[i-1]:
                cur+=1
                if flag == 0:
                    i+=1
                    cur=1
                    break
                if flag == 1:
                    flag = 2
                count = max(count,cur)
                i+=1
        if count <= 2:
            return 0
        if flag != 2:
            return count
        count = max(count,cur)
        return count
