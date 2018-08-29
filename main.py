class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    # can initially pass in a list to append to this LinkedList upon initialization
    def __init__(self, other_list=None):
        self.size = 0
        self.head = None
        self.tail = None
        if other_list is not None:
            for item in other_list:
                self.append(item)

    # checks to see if this list is empty based on the size variable
    def is_empty(self):
        return self.size == 0

    # adds a new node to this list with the given data
    def append(self, data):
        new_node = Node(data)
        if self.size <= 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # returns an array containing each element in the list in order that the
    # elements occur in the list
    def convert_to_arr(self):
        list = []
        curr_node = self.head
        while curr_node is not None:
            list.append(curr_node.data)
            curr_node = curr_node.next
        return list

    # appends another list to the end of this list
    def append_list(self, other_list):
        if other_list is not None:
            if isinstance(other_list, LinkedList):
                for item in other_list.convert_to_arr():
                    self.append(item)
            else:
                for item in other_list:
                    self.append(item)

    # prints out each element in the list in order
    def __str__(self):
        result = '['
        curr_node = self.head
        for i in range(self.size - 1):
            result += str(curr_node.data) + ', '
            curr_node = curr_node.next
        if curr_node is not None:
            result += str(curr_node.data)
        result += ']'
        return result

    # gets the data from a node at a certain index
    def get(self, index):
        if index >= self.size or index < 0:
            print("Error: index must be within the size of the list")
            return None
        if index == self.size - 1:
            return self.tail.data
        curr_node = self.head
        idx = 0
        while idx != index:
            curr_node = curr_node.next
            idx += 1
        return curr_node.data

    # removes a node from the list based on the given index
    def remove_by_index(self, index):
        if index >= self.size or index < 0:
            print("Error: index must be within the size of the list")
        else:
            if self.size == 1:
                self.head = None
                self.tail = None
            elif index == 0:
                self.head = self.head.next
            elif index == self.size - 1:
                curr_node = self.head
                while curr_node.next.next is not None:
                    curr_node = curr_node.next
                self.tail = curr_node
                self.tail.next = None
            else:
                curr_node = self.head
                for i in range(index - 1):
                    curr_node = curr_node.next
                curr_node.next = curr_node.next.next
            self.size -= 1

    # removes a node from the list based on the which data is chosen
    def remove_by_item(self, data):
        if self.size > 0:
            trail_node = self.head
            curr_node = self.head
            while curr_node.data != data:
                curr_node = curr_node.next
                if curr_node is None or curr_node.data == data:
                    break
                trail_node = trail_node.next
            if curr_node is not None:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                elif trail_node == curr_node == self.head:
                    self.head = self.head.next
                else:
                    trail_node.next = curr_node.next
                    if curr_node == self.tail:
                        self.tail = trail_node
                    curr_node = None
                self.size -= 1
            else:
                print("Item is not present in list")

    # returns the index location of a certain node containing the chosen data
    # returns -1 if the chosen data is not currently in the list
    def index_of(self, data):
        idx = 0
        curr_node = self.head
        while curr_node is not None and curr_node.data != data:
            curr_node = curr_node.next
            idx += 1
        return -1 if curr_node is None else idx

    # returns true if this LinkedList object is equal to the passed LinkedList object
    # returns false if the passed object is not a LinkedList object or if the passed LinkedList
    # is not equal to the calling list
    def equals(self, other_list):
        result = isinstance(other_list, LinkedList)
        if result:
            result = self.size == other_list.size
            if result:
                self_node = self.head
                other_node = other_list.head
                while result and self_node is not None:
                    result = self_node.data == other_node.data
                    self_node = self_node.next
                    other_node = other_node.next
        return result

