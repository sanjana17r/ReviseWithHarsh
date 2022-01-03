def getNthUglyNo(self,n):
		# code here
		l2,l3,l5=0,0,0
		arr = [1]
		count = 1
		while count<n:
		    cur2 = arr[l2]*2
		    cur3 = arr[l3]*3
		    cur5 = arr[l5]*5
		    cur = min(cur2,cur3,cur5)
		    if cur == cur2:
		        l2+=1
		    if cur == cur3:
		        l3+=1
		    if cur == cur5:
		        l5+=1
		    arr.append(cur)
		    count+=1
		return arr[-1]
