# stack creation

'''stack = []
def push():
    ele = int(input("enter the element"))
    stack.append(ele)
    print(stack)

def pop():
    if not stack:
        print("stack is empty")

    else:
        e = stack.pop()
        print("select operation 1.push 2.pop 3.quit")
        print(stack)

while True:

    print (" select operations 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop ()
    elif choice==3:
        break
    else:
        print ("print current operation",stack)'''



class node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class stack:
    def __init__ (self):
        self.head=None
    def isempty(self):
        if self.head=None:
            self.head = node(data)
        else:
            new - node(data)
            new.next = self.head
            self.head = new
    def pop(self):
        if self.empty():
            return None
        else:
            pnode=self.head
            self.head=self.head.next
            pnode.next=None
            return pnode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t = self.head
        if self.isempty():
            print("satck underflow")
        else:
            while (t!=None):
                print(t.data,end="")
                t=t.next
                if(t!=None):
                    print("-->",end=" ")


            return

if __name__ == "__main__":
    s = stack()
    s.push(2)
    s.push(4)
    s.push(6)
    s.push(8)
    s.push(10)
    s.display()
    print()
    print(s.peek())
    s.pop()
    s.peek()
    s.display()



s = input()
st=[]
balanced=True
for char is s:
    if(char=="(" or char =="{" or char=="["):
        stack.append(char)




