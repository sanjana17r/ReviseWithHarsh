def find3number(self,A, n):
        # code here
        m1,m2 = float('inf'),float('inf')
        in1,in2 = n,n
        in3 = n
        m3 = float('inf')
        for i in range(len(A)):
            if A[i]<=m1:
                if i<in2:
                    in1 = i
                    m1 = A[i]
            elif A[i]<=m2:
                if i<in3:
                    in2 = i
                    m2 = A[i]
            elif A[i]<=m3:
                m3 = A[i]
                # print('-------',[m1,m2,m3])
                return [m1,m2,m3]
        # print('----------')
        if m1 == m2 or m2 == m3 or m1 == m3:
            # print('empty')
            return []
        if m1 == float('inf') or m2 == float('inf') or m3 == float('inf'):
            # print('empty 2')
            return []
        # print("arr is ",[m1,m2,m3])
        return [m1,m2,m3]
