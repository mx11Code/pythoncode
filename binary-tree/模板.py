class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val, self.left, self.right = val, left, right


vals = [8, 4, -1, 2, -1, 5, 9, 1, -1, 6, 10, 3, 11, 7, 12]

nodes = [TreeNode(i) for i in vals]


def create_tree(orphan_nodes):
    if not orphan_nodes:
        return None
    len_nodes = len(orphan_nodes)
    if len_nodes == 1:
        return orphan_nodes[0] if orphan_nodes[0].val != -1 else None

    mid = int((len_nodes - 1) / 2)
    left, right = create_tree(orphan_nodes[:mid]), create_tree(orphan_nodes[mid + 1:])
    root = orphan_nodes[mid]

    if root.val == -1:
        return None

    root.left, root.right = left, right
    return root


tree_root = create_tree(nodes)


def in_order_recursion(root):
    if not root:
        return

    if not root.left and not root.right:
        print(root.val)
    else:
        if root.left:
            in_order_recursion(root.left)
        else:
            print(-1)

        print(root.val)

        if root.right:
            in_order_recursion(root.right)
        else:
            print(-1)


def pre_order_stack(root):
    stack = [root]
    val = []
    while stack:
        current = stack.pop()
        if not current:
            val.append(-1)
            continue
        val.append(current.val)
        if current.left or current.right:
            stack.append(current.right if current.right else None)
            stack.append(current.left if current.left else None)
    print(val)


def post_order_stack(root):
    stack = [root]
    result = []
    picked = []
    while stack:
        current = stack.pop()
        if not current:
            result.append(-1)
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


def in_order_stack(root):
    stack = [root]
    result = []
    picked = []
    while stack:
        current = stack.pop()
        if not current:
            result.append(-1)
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


print(in_order_stack(tree_root))
