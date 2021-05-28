""" 
https://leetcode.com/problems/linked-list-cycle/
"""

import linked_list
null = None

def hasCycle(head):
    if not head:
        return False
    slow, fast = head, head
    
    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def run():
    testCases = [([3,2,0,-4], 1), ([1,2], 0), ([1], -1) ]
    for testCase in testCases:
        print(testCase)
        inputList, position = testCase
        testList = linked_list.createList(inputList)
        testList = linked_list.addCycle(testList, position)
        print(hasCycle(testList))
        print("\n\n")