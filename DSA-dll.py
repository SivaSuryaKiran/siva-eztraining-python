# insertion into double linked list 

'''class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def insert_beg(self):
        print("start",end=" ")
        n = Node(400)
        temp = self.head
        temp.previous = n
        n.next = temp
        self.head = n
    def display(self):
        if self.head is None :
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp = temp.next
            print("end")

l = dll()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
n3 = Node(300)
n2.next = n3
n3.previous = n2
l.insert_beg()
l.display()'''
                
# double linked list creation

'''class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None :
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp = temp.next

l = dll()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
n3 = Node(300)
n2.next = n3
n3.previous = n2
l.display()'''


'''class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def insert_pos(self,pos):
        print("start",end="")
        n = Node(400)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        n.previous = temp
        n.next = temp.next
        temp.next.previous = n
        temp.next = n
    def display(self):
        if self.head is None :
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp = temp.next
            print("end")
l = dll()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
n3 = Node(300)
n2.next = n3
n3.previous = n2
l.insert_pos(3)
l.display()'''



# deletion at beg in dll

'''class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def delete_beg(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def display(self):
        if self.head is None :
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp = temp.next
            print("end")
l = dll()
print("start",end = " ")
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
n3 = Node(300)
n2.next = n3
n3.previous = n2
l.display()
l.delete_beg()
l.display()'''


# deletion at end in dll


'''class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def delete_end(self):
        temp = self.head.next
        previous = self.head
        while temp.next is not None:
            temp = temp.next
            previous = previous.next
        previous.next = temp.next
        temp.next = None

    def display(self):
        if self.head is None :
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp = temp.next
            print("end")
l = dll()
print("start",end = " ")
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
n3 = Node(300)
n2.next = n3
n3.previous = n2
print("before deletion")
l.display()
l.delete_end()
print("after deletion")
l.display()'''

# deletion  from position 

class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def delete_pos(self,pos):
        temp = self.head.next
        previous = self.head
        for i in range(1,pos-1):
            temp = temp.next
            previous = previous.next
        previous.next = temp.next
        temp.next = None

    def display(self):
        if self.head is None :
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp = temp.next
            print("end")
l = dll()
n1 = Node(100)
l.head = n1
n2 = Node(200)
n2.previous = n1
n1.next = n2
n3 = Node(300)
n2.next = n3
n3.previous = n2
print("before deletion",end="   ")
l.display()
l.delete_pos(2)
print("after deletion",end="   ")
l.display()


