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
