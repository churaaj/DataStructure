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
            node.next = tptr.next
            tptr.next = node
        else:
            print("No element found")
    
    def append(self, data):
        node = Node(data)
        tptr = self.head
        while tptr.next != None:
            tptr = tptr.next

        tptr.next = node


    def display(self):
        tptr = self.head
        while tptr != None:
            print(tptr.data,end=" ")
            tptr = tptr.next
        print()
        
        
    def getcount(self, node):
        if node == None:
            return 0
        else:
            return 1 + self.getcount(node.next)

    def length(self):
        return self.getcount(self.head)

    def reverse(self):
        current = self.head
        prev = None
        after = self.head

        while current:
            after = after.next
            current.next = prev
            prev = current
            current = after

        self.head = prev

link = LinkedList()
link.push(3)
link.push(5)
link.insert(4,5)
link.append(2)
link.display()
l = link.length()
print("The length of list is",l)
link.reverse()
link.display()
