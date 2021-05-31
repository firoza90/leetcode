"""
https://leetcode.com/problems/merge-two-sorted-lists/
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
 #Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        print(self.val)
        next = self.next
        while(next):
            print(next.val)
            next = next.next

def createList(arr):
    result = None
    arr = arr[::-1]
    for item in arr:
        result = ListNode(item, result)
    return result

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1

        #l1 will always be the starting point
        curr1, curr2 = l1, l2
        next, temp = l1.next, None

        if not next:
            l1.next = l2
            return l1

        while next and curr2:
            if curr2.val >= curr1.val and curr2.val <= next.val:
                temp = curr2.next
                curr2.next = next
                curr1.next = curr2

                #update curr1 and curr2
                curr1 = curr2
                curr2 = temp
            else:
                if next.next:
                    next = next.next
                    curr1 = curr1.next
                else:
                    next.next = curr2
                    return l1
        return l1

    def test_mergeTwoLists(self):
        testcases = []
        for testcase in testcases:
            l1 = createList(testcase[0])
            l2 = createList(testcase[1])
            print(l1.toString())
            print(l2.toString())
            print(self.mergeTwoLists(l1, l2).toString())

