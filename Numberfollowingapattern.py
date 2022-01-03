def printMinNumberForPattern(ob,s):
        # code here 
        ans = ''
        st = []
        num = 1;
        for it in s:
            if(it == 'D'):
                st.append(num)
                num+=1
            else:
                st.append(num)
                num+=1
                while(st):
                    ans += str(st[-1])
                    st.pop()
        st.append(num)
        while(st):
            ans += str(st[-1])
            st.pop()
        return ans
