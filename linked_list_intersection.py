"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
"""

from linked_list import ListNode, createList

class Solution:
    ### O(n) Space Complexity
    #def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #    stackA = []
    #    ptr = headA
    #    while (ptr):
    #        stackA.append(ptr)
    #        ptr = ptr.next

    #    stackB = []
    #    ptr = headB
    #    while (ptr):
    #        stackB.append(ptr)
    #        ptr = ptr.next

    #    result = None
    #    while (stackA and stackB and stackA[-1] == stackB[-1]):
    #        result = stackA[-1]
    #        stackA.pop()
    #        stackB.pop()
    #    return result.val

    ### O(1) space complexity
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA = 0
        ptr = headA
        while ptr:
            lengthA = lengthA + 1
            ptr = ptr.next

        lengthB = 0
        ptr = headB
        while ptr:
            lengthB = lengthB + 1
            ptr = ptr.next

        diff = lengthA - lengthB

        
        ptrA = headA
        ptrB = headB
        if diff < 0:
            # LL A is shorter, traverse B
            diff = abs(diff)
            while (diff > 0):
                ptrB = ptrB.next
                diff = diff - 1
        else:
            while (diff > 0):
                diff = abs(diff)
                ptrA = ptrA.next 
                diff = diff - 1

        while (ptrA and ptrB):
            if ptrA == ptrB:
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next

        return None

    def test_getIntersectionNode(self):
        testcases = []
        for testcase in testcases:
            print(testcase)
            l1 = createList(testcase[0])
            l2 = createList(testcase[1])
            intersection = self.getIntersectionNode(l1, l2)
            if intersection:
                print(intersection.val)
            else:
                print('No intersection')
