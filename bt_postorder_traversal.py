
"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""
from binary_tree import TreeNode, createTree
null = None


def run():
    testCases = [[1,null,2,3], [], [1]]
    for testCase in testCases:
        print(testCase)
        tree = createTree(testCase)
        print(preorderTraversal(tree))
        print("\n\n")

def postorderTraversal(root):
    if not root:
        return []
    result = []
    result.extend(postorderTraversal(root.left))
    result.extend(postorderTraversal(root.right))
    result.append(root.val)
    return result
