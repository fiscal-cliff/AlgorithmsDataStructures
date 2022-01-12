class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):

        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all = False):

        if self.head.value == val:
            self.head = self.head.next
        elif self.tail.value == val:
            node = self.head
            while node.next != self.tail:
                node = node.next
            self.tail = node
            node.next = None
        else:
            node = self.head
            while True:
                prev = node
                node = node.next
                if node.value == val:
                    prev.next = node.next
                    return node
                if node is None:
                    break
        if all:
            count = 0
            node = self.head
            while node is not None:
                if node.value == val:
                    count += 1
                node = node.next
            for i in range(count):
                if self.head.value == val:
                    self.head = self.head.next
                elif self.tail.value == val:
                    node = self.head
                    while node.next != self.tail:
                        node = node.next
                    self.tail = node
                    node.next = None
                else:
                    node = self.head
                    previous = node
                    node = node.next
                    while node != self.tail:
                        if node.value == val:
                            previous.next = node.next
                            node = node.next
                            # previous = previous.next
                        else:
                            node = node.next
                            previous = previous.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):

        if self.head is None:
            return 0

        node = self.head
        count = 1
        while node.next != None:
            node = node.next
            count += 1
        return count

    def insert(self, afterNode, newNode):

        if afterNode is None:
            node_for_insert = Node(newNode)
            node_for_insert.next = self.head
            self.head = node_for_insert
        else:
            node_for_insert = Node(newNode)
            node = self.head  
            while node is not None:
                if node.value == afterNode:
                    buffered_item = node.next
                    node.next = node_for_insert
                    break
                else: node = node.next

            node_for_insert.next = buffered_item

            if self.tail.value == afterNode:
                self.tail = node_for_insert
