"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        if not T2:
            return True
        if not T1:
            return False
        return self.is_same_tree(T1, T2) or self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

    def is_same_tree(self, T1, T2):
        if not T1 and not T2:
            return True
        if T1 and T2:
            return T1.val == T2.val and self.is_same_tree(T1.left, T2.left) and self.is_same_tree(T1.right, T2.right)
        return False
