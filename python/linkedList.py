class Node:
    value = None
    next = None

head = Node()
head.value = "head"
last = head
lst = range(0, 20, 2)
for i in lst:
    n = Node()
    n.value = i
    last.next = n
    last = n


def print_linked_list(linked_list_head):
    current = linked_list_head
    while current.next:
        print(current.value)
        current = current.next
    print(current.value)


def insert(linked_list_head, pos, node):
    current_pos = 0
    current_node = linked_list_head
    while current_pos < pos - 1:
        current_node = current_node.next
        current_pos += 1
    target_pos_node = current_node.next
    node.next = target_pos_node
    current_node.next = node


node_to_be_insert = Node()
node_to_be_insert.value = "node_to_be_insert"
insert(head, 2, node_to_be_insert)
print_linked_list(head)


def append(linked_list_head, node):
    current = linked_list_head
    while current.next:
        current = current.next
    current.next = node

node_to_be_append = Node()
node_to_be_append.value = "node_to_be_append"
append(head, node_to_be_append)
# print_linked_list(head)


def remove(linked_list_head, pos):
    current_pos = 0
    current_node = linked_list_head
    while current_pos < pos - 1:
        current_node = current_node.next
        current_pos += 1
    current_node.next = current_node.next.next


def pop(linked_list_head):
    pass



