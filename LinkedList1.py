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

    def delete(self, val, all_flag=False):

        node = self.head
        while node is not None:

            if self.len() == 1 and self.head.value == val:
                self.head = None
                self.tail = None
                node = None
                break

            if self.head.value == val:
                self.head = self.head.next
                node = node.next

            else:
                node = self.head.next
                previous = self.head
                while node is not None:
                    if node.value == val and self.len() == 1:
                        self.head = None
                        self.tail = None
                        node = None
                    elif node.value == val:
                        previous.next = node.next
                        if node.next is None:
                            self.tail = previous
                        if not all_flag:
                            break
                    else:
                        previous = node
                    node = node.next

            if self.len() == 1:
                break
                if not all_flag:
                    break

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
            node_for_insert = Node(newNode)  # создать новый узел
            node = self.head  # найти узел афтернод и сохранить в буфер его следующий элемент, присвоить ему следующий элемент = новый узел
            while node is not None:
                if node.value == afterNode:
                    buffered_item = node.next
                    node.next = node_for_insert
                    break
                else:
                    node = node.next

            node_for_insert.next = buffered_item

            if self.tail.value == afterNode:
                self.tail = node_for_insert
