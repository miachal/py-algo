from node import Node

class LinkedList():
    def __init__(self):
        self._root = None
        self._last = None
        self._size = 0

    # TODO
    # add_before

    def add(self, data):
        new_node = Node(data)

        if self._size == 0:
            self._root = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node

        self._size += 1

    def add_after(self, node, data):
        new_node = Node(data)

        this_node = self._root
        while this_node.next:
            if this_node == node:
                new_node.next = this_node.next
                this_node.next = new_node
                self._size += 1

            this_node = this_node.next

    def add_at_the_beggining(self, data):
        new_node = Node(data)

        new_node.next = self._root
        self._root = new_node

        self._size += 1

    def add_at_the_end(self, data):
        new_node = Node(data)

        self._last.next = new_node
        self._last = new_node

        self._size += 1

    def find(self, data):
        node = self._root

        for i in range(self._size):
            if node.data == data:
                return node
            else:
                node = node.next

        return None

    # TODO
    # remove_node?

    def remove(self, data):
        node = self._root
        while node.next:
            if node.next.data == data:
                node.next = node.next.next if node.next.next else None # ekhm.
                self._size -= 1
            node = node.next

    def __repr__(self):
        node = self._root
        out = '({} items): {}'.format(self._size, node.data)
        while node.next:
            node = node.next
            out += ' -> {}'.format(node.data)
        return out

    def __len__(self):
        return self._size


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add(10)
    linked_list.add(20)
    linked_list.add(30)
    print(linked_list)

    node = linked_list.find(20)
    print('Data: {}, Next: {}'.format(node.data, node.next))

    linked_list.add_after(node, 25)
    linked_list.add_after(Node(24), 26)
    print(linked_list)

    linked_list.remove(20)
    print(linked_list)

    linked_list.add_at_the_end(120)
    print(linked_list)

    linked_list.add_at_the_beggining(200)
    print(linked_list)