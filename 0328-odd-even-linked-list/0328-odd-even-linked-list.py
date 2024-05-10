# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        curr  = head.next 
        x= curr
        i = 1
        # print(pre)
        # print(x)
        while curr and curr.next:
            pre.next = curr.next
            pre = pre.next
            curr.next = pre.next
            curr = curr.next

        
        pre.next = x
        return head
            

        



        # if not head or not head.next:
        #     return head

        # odd = head
        # even = head.next
        # even_head = even

        # while even and even.next:
        #     odd.next = even.next
        #     odd = odd.next
        #     even.next = odd.next
        #     even = even.next

        # odd.next = even_head

        # return head
                

            