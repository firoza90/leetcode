"""
https://leetcode.com/problems/implement-queue-using-stacks/
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []
        self.topvalue = None
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.b.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.a) == 0:
            while len(self.b) != 0:
                self.a.append(self.b.pop())
        return self.a.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        val = None
        if len(self.a) == 0:
            while len(self.b) != 0:
                val = self.b.pop()
                self.a.append(val)
        return self.a[-1]
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.a) == 0 and len(self.b) == 0

class MyQueueOperation:
    myQueue = "MyQueue"
    push = "push"
    pop = "pop"
    top = "peek"
    empty = "empty"


class Solution:
    # Your MyQueue object will be instantiated and called as such:
    # obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()
    def test_queueFromStack(self):
        def validQueue(myQueue):
            if not myQueue:
                print("Cannot perform operation : %s" %operations[i])
                return False
            else:
                return True
        testcases = [(["MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"] , [[],[1],[2],[3],[4],[],[5],[],[],[],[]]), 
                     (["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]),
                     (["MyQueue","push","pop","empty"], [[],[1],[],[]])]
        for testcase in testcases:
            result = []
            operations, values = testcase
            myQueue = None
            for i in range(0, len(operations)):
                if operations[i] == MyQueueOperation.myQueue:
                    myQueue = MyQueue()
                    result.append(None)
                elif operations[i] == MyQueueOperation.push:
                    if not validQueue(myQueue):
                        break
                    myQueue.push(values[i][0])
                    result.append(None)
                elif operations[i] == MyQueueOperation.pop:
                    if not validQueue(myQueue):
                        break
                    result.append(myQueue.pop())
                elif operations[i] == MyQueueOperation.top:
                    if not validQueue(myQueue):
                        break
                    result.append(myQueue.peek())
                elif operations[i] == MyQueueOperation.empty:
                    if not validQueue(myQueue):
                        break
                    result.append(myQueue.empty())
            print(result)