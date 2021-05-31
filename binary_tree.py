"""
Binary Tree functionalities
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        from collections import deque
        q = deque()
        node = self
        q.append(node)
        result = []
        while q:
            node = q.popleft()
            result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(result)

def createTree(tree):
    if not tree:
        return None
    nodes = [None if item == None else TreeNode(item) for item in tree]
    child = nodes[::-1]
    root = child.pop()
    curr = root
    for node in nodes:
        if node:
            if child:
                node.left = child.pop()
            if child:
                node.right = child.pop()
    return root


    
