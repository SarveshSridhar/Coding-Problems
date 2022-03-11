class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []
        tail = ListNode(0)
        temp = tail
        while head:
            a.append(head.val)
            head = head.next
        print(a)
        if len(a)>0:
            k = k%len(a)
        result = a[len(a)-k:] + a[:len(a)-k]
        for i in range(len(result)):
            temp.next = ListNode(result[i])
            temp = temp.next
        return tail.next
