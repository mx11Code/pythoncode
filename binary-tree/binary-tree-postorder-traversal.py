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
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal1(self, root):
        # write your code here
        result = []
        stack = []
        pre = None
        if root:
            stack.append(root)
        while stack:
            cur = stack[-1]
            if cur.left == cur.right == None or (pre and (pre == cur.left or pre == cur.right)):
                result.append(cur.val)
                stack.pop()
                pre = cur
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return result

    def postorderTraversal2(self, root):
        if not root:
            return []
        stack = [root]
        picked = []
        result = []
        while stack:
            current = stack.pop()
            if not current:
                continue
            is_leaf = not current.left and not current.right
            picked_before = bool(picked) and current == picked[-1]
            if is_leaf or picked_before:
                result.append(current.val)
                if not is_leaf and picked:
                    picked.pop()
            else:
                picked.append(current)
                stack.append(current)
                stack.append(current.right if current.right else None)
                stack.append(current.left if current.left else None)

        return result
