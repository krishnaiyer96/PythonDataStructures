from tempfile import tempdir


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = -1

    def print_list(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        dl = ''
        while temp is not None:
            dl += str(temp.value) + '<-->'
            temp = temp.next
        print(dl)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp
    def prepand(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    def pop_first(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        temp = self.head
        self.head.next = temp
        temp.prv = None
        self.head = temp



if __name__ == '__main__':
    dll = DoublyLinkedList(5)
    dll.append(10)
    dll.print_list()
    dll.append(11)
    dll.print_list()
    dll.pop()
    dll.print_list()
    dll.prepand(15)
    dll.print_list()
