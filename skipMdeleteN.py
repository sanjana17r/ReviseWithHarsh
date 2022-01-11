def skipMdeleteN(self, head, M, N):
        # Code here
        cur = head
        if M == 0:
            return None
        
        while cur:
            count = 1
            while cur.next and count<M:
                cur = cur.next
                count+=1
            cur2 = cur
            count = 1
            while cur2.next and count<=N:
                cur2 = cur2.next
                count+=1
            cur.next = cur2.next
            cur = cur.next
        return head
