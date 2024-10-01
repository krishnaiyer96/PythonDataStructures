class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# Printing the value of the elements in the Linked List
    def print_list(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        ll = ''
        while temp is not None:
            ll += str(temp.value) + '-->'
            temp = temp.next
        print(ll)
    # Appending the value at the end in the Linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        pre = self.head
        temp = self.head
        if self.head is None:
            print("List is empty")
        elif self.length == 0:
            self.head = None
            self.tail = None
        else:
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        return temp.value

    def prepand(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def insert_node(self, value, index):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        count = 0
        while temp:
            if count == index - 1:
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next
            count +=1

    def remove_at(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            self.head = None
            self.tail = None
        if index == 0:
            self.head = self.head.next
        temp = self.head
        count = 0
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1
        self.length -= 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length - 1):
            after = temp.next
            temp.next = before
            before = temp
            temp = after














if __name__ == '__main__':
    my_linked_list = linked_list(4)
    my_linked_list.append(10)
    my_linked_list.append(15)
    my_linked_list.append(20)
    my_linked_list.append(30)
    my_linked_list.append(40)
    my_linked_list.print_list()
    my_linked_list.pop()
    my_linked_list.print_list()
    my_linked_list.prepand(5)
    my_linked_list.print_list()
    my_linked_list.pop_first()
    my_linked_list.print_list()
    num = my_linked_list.get(2)
    print(num)
    my_linked_list.insert_node(6, 2)
    my_linked_list.print_list()
    my_linked_list.remove_at(2, 6)
    my_linked_list.print_list()
    my_linked_list.remove_at(0, 4)
    my_linked_list.print_list()
    my_linked_list.reverse()
    my_linked_list.print_list()





    










