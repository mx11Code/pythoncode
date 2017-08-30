"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        first_root = [root]
        while first_root:
            value_of_root = []
            children_of_root = []
            for node in first_root:
                value_of_root.append(node.val)
                if node.left:
                    children_of_root.append(node.left)
                if node.right:
                    children_of_root.append(node.right)
            result.append(value_of_root)
            first_root = children_of_root
        return result