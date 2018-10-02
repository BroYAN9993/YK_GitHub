# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        p = head
        while p:
            vals.append(p.val)
            p = p.next
        while len(vals) > 1:
            if vals[0] == vals[-1]:
                vals.pop()
                vals.pop(0)
            else:
                return False
        return True
