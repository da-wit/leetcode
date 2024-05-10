# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # x = []
        # curr = head
        # while curr:
        #     x.append(curr.val)
        #     curr = curr.next
        # print(x)
        
        # if x == x[::-1]:
        #     return True
        # print(head)
        # temp = head./
        # curr = head
        # next = None
        # prev =None
        # while curr and temp:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # #temp = temp.next
         
        curr = head
        x = []
        while curr:
            x.append(curr.val)
            curr =curr.next
        
        return x ==x[::-1]

       
        