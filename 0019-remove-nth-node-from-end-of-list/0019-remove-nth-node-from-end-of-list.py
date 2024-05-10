# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(head):
            curr = head
            count =0
            while curr:
                curr = curr.next
                count +=1
            return count
        
        # print(length(head) )
        x = length(head) 
        # print(x)
        # def first(head):
        #     curr = head
        #     head = curr.next
        #     curr.next = None
            
            
        y = x - n
        def delete(head,y):
            pre = head
            curr = head.next
            for i in range(1,y):
                pre = pre.next
                curr = curr.next
            pre.next = curr.next
            curr.next = None

        if n == x:
            head = head.next
        elif n == 1:
            pre = head
            curr = head.next
            while curr.next:
                pre = pre.next
                curr = curr.next
            pre.next = None
        else:
            delete(head,y)


        
        return head
        
            

        # print(delete(head,x))
            
        