"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1->1->2
Output: 1->2
"""

from linked_list import ListNode, createList

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        ptr = head
        pptr = head.next

        while(pptr):
            while pptr.val == ptr.val:
                ptr.next = pptr.next
            ptr = pptr
            pptr = pptr.next

        return head

l1 = createList([])
sol = Solution()
sol.deleteDuplicates(l1).toString()
