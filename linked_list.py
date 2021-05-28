"""
Linked List Utils
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        result = str(self.val)
        next = self.next
        while(next):
            result = result + " -> " + str(next.val)
            next = next.next
        print(result)

def createList(arr):
    result = None
    arr = arr[::-1]
    for item in arr:
        result = ListNode(item, result)
    return result

def addCycle(head, pos):
    if pos == -1:
        return head
    ptr, pptr = head, head
    while ptr:
        pptr = ptr
        ptr = ptr.next
    tail = pptr
    ptr = head
    for i in range(0, pos):
        ptr = ptr.next
    tail.next = ptr
    print("Cycle add at %d location with %d value" %(pos, ptr.val))
    return head