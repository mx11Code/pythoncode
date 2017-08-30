class LinkedNode:
    def __init__(self, val):
        self.next = None
        self.val = val


head = LinkedNode(0)
current = head
for i in range(1, 10):
    node = LinkedNode(i)
    current.next = node
    current = node


def print_linked_list(head):
    lst = []
    c = head
    while c:
        lst.append(c.val)
        c = c.next
    print(" -> ".join([str(v) for v in lst]))


# print_linked_list(head)


def swap_nodes_in_pairs(head):
    l = None
    c = head
    new_head = c.next
    while c:
        n = c.next
        r = n.next

        n.next = c
        if r:
            c.next = r
        else:
            c.next = None

        if l:
            l.next = n
        l = c
        if r:
            c = r
        else:
            break
    return new_head


new_head = swap_nodes_in_pairs(head)
print_linked_list(new_head)
