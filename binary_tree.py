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

def _insertLevelOrder(arr, root, i, n):
    if i < n:
        if not arr[i]:
            return None
        root = TreeNode(arr[i])
        root.left = _insertLevelOrder(arr, root.left, 2*i+1, n)
        root.right = _insertLevelOrder(arr, root.right, 2*i+2, n)
    return root

def createTree(tree):
    if not tree:
        return None
    root = None
    root = _insertLevelOrder(tree, root, 0, len(tree))
    return root


    
