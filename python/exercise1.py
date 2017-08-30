class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        result = []
        path = []
        if not root:
            return result
        path.append(root.val)
        self.func(root, path, root.val, target, result)
        return result

    def func(self, root, path, sum, target, result):
        if not root.left and not root.right:
            if sum == target:
                result.append(path)
            return
        if root.left:
            path.append(root.left.val)
            self.func(root.left, path, sum + root.left.val, target, result)
            path.remove(len(path) - 1)
        if root.right:
            path.append(root.right.val)
            self.func(root.right, path, sum + root.right.val, target, result)
            path.remove(len(path) - 1)
