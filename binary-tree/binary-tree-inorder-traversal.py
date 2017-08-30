"""
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal1(self, root):
        result = []
        stack = []
        cur = root
        while cur or len(stack) != 0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result

    def inorderTraversal2(self, root):
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
                stack.append(current.right if current.right else None)
                stack.append(current)
                stack.append(current.left if current.left else None)
        return result
