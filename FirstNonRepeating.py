def FirstNonRepeating(self, A):
		f = 0
		res = ''
		s = {}
		for i in range(len(A)):
		    if A[i] in s:
		        s[A[i]]+=1
		    else:
		        s[A[i]]=1
		    if A[i] in s:
		        while (A[f] == A[i] or s[A[f]] >1) and f<i:
		            if (A[f] in s):
		                if s[A[f]]>1:
		                    f+=1
		                else:
		                    break
		        if (s[A[f]]>1):
		            res+='#'
		            f+=1
		        else:
		            res+=A[f]
		    else:
		        res+=A[f]
		return res
