# declaring a class for Node and assign value

class Node:

    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    # function for pushing a data:

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self,data,to_check):
        tptr = self.head
        flag = 0
        node = Node(data)

        while tptr != None:
            if tptr.data == to_check:
                flag = 1
                break
            tptr = tptr.next

        if flag == 1:
            node.next = tptr
            tptr.next = node


    def display(self):
        tptr = self.head
        while tptr != None:
            print(tptr.data)
            tptr = tptr.next

link = LinkedList()
link.push(3)
link.push(5)
link.insert(4,5)
link.display()


    
