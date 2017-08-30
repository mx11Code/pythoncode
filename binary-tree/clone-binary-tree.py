"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    def cloneTree(self, root):
        if root:
            new_root = TreeNode(root.val)
        else:
            return None
        new_root.left = self.cloneTree(root.left)
        new_root.right = self.cloneTree(root.right)
        return new_root