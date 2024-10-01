class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        if self.first is None:
            print('Queue is empty')
        temp = self.first
        queue = ''
        while temp is not None:
            queue = temp.value
            temp = temp.next
            print(queue)
    def enqueue(self,value):
        new_node = Node(value)
        if self.length == 1:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    def dequeue(self):
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1




my_queue = Queue(10)
my_queue.enqueue(15)
my_queue.enqueue(20)
my_queue.enqueue(25)
my_queue.enqueue(30)
print('Queue after enqueuing new element')
my_queue.print_queue()

my_queue.dequeue()
print('\n queue after de queueing the element')
my_queue.print_queue()
