'''queue=[]
def enqueue():
    element = input("enter element")
    queue.append(element)
    print(element,"is  added in queue")

def dequeue():
    if not queue:
        print("Q is empty")
    else:
        e = queue.pop(0)
        print("removed element",e)

def display():
    print(queue)

while True:
    print("select operation 1.add 2.delete 3.display")
    choice=int(input())
    if choice==1:
        enqueue()
    if choice==2:
        dequeue()
    if choice==3:
        display()
    if choice==4:
        break'''

'''
from queue import LifoQueue
n = LifoQueue(maxsize=3)
print(n.qsize())
n.put("s")
n.put("b")
n.put("c")
print(n.full())
print(n.qsize())
print(n.get())
print(n.get())
print(n.get())
print(n.empty())'''

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__ (self):
        self.head = None
        self.last = None
    def enqueue(self,data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.data = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return

a_queue = Queue()
while True:
    print("enqueue<value>")
    print("dequeue")
    print("quit")
    do = input("what would be like to do").split()
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation == 'dequeue':
        dequeued = a_queue.dequeue()
        if dequeued is None:
            print("Queue is empty")
        else:
            print("dequeued elements ",int(dequeued))

    elif operation =='quit':
        break
