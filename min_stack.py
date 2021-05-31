"""
https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        elif val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min = self.min[:-1]

    def top(self) -> int:
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        min = self.min[-1]
        return min
        
class MinStackOperation:
    minStack = "MinStack"
    push = "push"
    pop = "pop"
    top = "top"
    getMin = "getMin"


class Solution:
    def test_minStackt(self):
        def validStack(minStack):
            if not minStack:
                print("Cannot perform operation : %s" %operations[i])
                return False
            else:
                return True
        testcases = [(["MinStack","push","push","push","getMin","pop","top","getMin"] , [[],[-2],[0],[-3],[],[],[],[]]),]
        for testcase in testcases:
            result = []
            operations, values = testcase
            minStack = None
            for i in range(0, len(operations)):
                if operations[i] == MinStackOperation.minStack:
                    minStack = MinStack()
                    result.append(None)
                elif operations[i] == MinStackOperation.push:
                    if not validStack(minStack):
                        break
                    minStack.push(values[i][0])
                    result.append(None)
                elif operations[i] == MinStackOperation.pop:
                    if not validStack(minStack):
                        break
                    minStack.pop()
                    result.append(None)
                elif operations[i] == MinStackOperation.top:
                    if not validStack(minStack):
                        break
                    result.append(minStack.top())
                elif operations[i] == MinStackOperation.getMin:
                    if not validStack(minStack):
                        break
                    result.append(minStack.getMin())
            print(result)