"""
https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from linked_list import ListNode, createList
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        ptr = head
        pptr = None

        while ptr:
            temp = ptr.next
            ptr.next = pptr
            pptr = ptr
            ptr = temp
        head = pptr
        return head

    def test_reverseList(self):
        tests = [[1,2,3,4,5], [1,2], []]
        for test in tests:
            print(test)
            l = createList(test)
            l = self.reverseList(l)
            if l:
                l.toString()
            else:
                print("Empty list")
