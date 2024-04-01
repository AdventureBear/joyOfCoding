class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



#Create a function to print any length list, given its head node.
# Test your function works by printing your list of 4 numbers.
def print_list(head):
    print(head.data, "->")
    if head.next_node is None:
        return
    print_list(head.next_node)


def remove_node(node_to_remove, head):
    # Store next node to reassign
    if node_to_remove.next_node is not None:
        next_pointer = node_to_remove.next_node
    else:
        return None
    print("next node: ", next_pointer.data)

    #find previous node by traversing list from head
    prev_node = find_prev_node(node_to_remove, head)
    print(prev_node.data)
    prev_node.next_node = next_pointer

    return


def find_prev_node(current, node_to_test):
    print("checking: ", current.data)
    if node_to_test.next_node == current:
        return node_to_test
    find_prev_node(node_to_test.next_node)
def main():
    new_node = Node("first node data")
    next_node = Node("second node data", new_node)
    # print(next_node.get_data())

    # Get this output by adding more dones
    # Fourth node -> Third node -> Second node -> First node
    third_node = Node("Third Node", next_node)
    fourth_node = Node("Fourth Node", third_node)

    print("\n")
    print("Print List")
    print("=" * 15)

    head = fourth_node
    while head is not None:
        print(head.get_data(), "->")
        head = head.get_next()

    # head = fourth_node
    #print_list(fourth_node)

    #After printing the list in main, remove a node & print the remaining  nodes.
    node_to_remove = third_node
    #print("=" * 15)
    print("\n")
    print("Removing nodes")
    print("=" * 15)
    print("Node to remove: ", node_to_remove.data)

    remove_node(third_node, fourth_node)
    print_list(fourth_node)

    #Next, add a new element & print your list.
    print("\n")
    print("Adding a node")
    print("=" * 15)


main()
