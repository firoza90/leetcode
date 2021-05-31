"""
https://leetcode.com/problems/implement-stack-using-queues/
Implement a last in first out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).
Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
"""

from collections import deque  
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = deque()
        self.b = deque()
        self.topvalue = None
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.a) != 0:
            self.a.append(x)
        else:
            self.b.append(x)
        self.topvalue = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.a) != 0:
            while len(self.a) != 1:
                self.topvalue = self.a.popleft()
                self.b.append(self.topvalue)

            return self.a.popleft()
        else:
            while len(self.b) != 1:
                self.topvalue = self.b.popleft()
                self.a.append(self.topvalue)
            return self.b.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.topvalue

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.a) == 0 and len(self.b) == 0


class MyStackOperation:
    myStack = "MyStack"
    push = "push"
    pop = "pop"
    top = "top"
    empty = "empty"


class Solution:
    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()
    def test_stackFromQueue(self):
        def validStack(myStack):
            if not myStack:
                print("Cannot perform operation : %s" %operations[i])
                return False
            else:
                return True
        testcases = [(["MyStack", "push", "push", "top", "pop", "empty"], [[], [1], [2], [], [], []]),]
        for testcase in testcases:
            result = []
            operations, values = testcase
            myStack = None
            for i in range(0, len(operations)):
                if operations[i] == MyStackOperation.myStack:
                    myStack = MyStack()
                    result.append(None)
                elif operations[i] == MyStackOperation.push:
                    if not validStack(myStack):
                        break
                    myStack.push(values[i][0])
                    result.append(None)
                elif operations[i] == MyStackOperation.pop:
                    if not validStack(myStack):
                        break
                    result.append(myStack.pop())
                elif operations[i] == MyStackOperation.top:
                    if not validStack(myStack):
                        break
                    result.append(myStack.top())
                elif operations[i] == MyStackOperation.empty:
                    if not validStack(myStack):
                        break
                    result.append(myStack.empty())
            print(result)