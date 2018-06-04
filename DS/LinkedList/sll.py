class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        node = self
        while node.next is not None:
            node = node.next
        new_node = Node(data)
        node.next = new_node

    def delete(self, data):
        node = self
        if self.data == data:
            return node.next

        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                return self
            node = node.next

        return self
