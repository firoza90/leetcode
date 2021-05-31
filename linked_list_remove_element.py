"""
https://leetcode.com/problems/remove-linked-list-elements/
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

from linked_list import ListNode, createList
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ptr, pptr = head, None
        while ptr:
            if ptr.val == val:
                if not pptr:
                    head = ptr.next
                else:
                    pptr.next = ptr.next
            else:
                pptr = ptr
            ptr = ptr.next
        return head

    def test_removeElements(self):
        testcases = [([1,2,6,3,4,5,6],6), ([], 1), ([7,7,7,7], 7)]
        for testcase in testcases:
            print(testcase)
            l = createList(testcase[0])
            l = self.removeElements(l, testcase[1])
            if l:
                l.toString()
            else:
                print('Empty list')

          