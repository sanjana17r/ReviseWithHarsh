    def displayContacts(self, n, contact, s):
        # code here
        res = []
        contact = list(set(contact))
        contact.sort()
        for i in range(len(s)):
            arr = []
            for j in contact:
                if j.startswith(s[:i+1]):
                    arr.append(j)
            if len(arr) == 0:
                arr = ['0']
            res.append(arr)
            contact = arr[:]
        return res
