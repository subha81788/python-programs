class Node:
    def __init__(self):
        self.data = 0
        self.link = None
    
    def __init__(self, data, n):
        self.data = data
        self.link = n
    
class StackLinkedList:

    private static final int MAX_SIZE = 100

    def __init__(self):
        self.tos = None
        self.size = 0

    def push(self, val):
        nptr = Node(val,None)
        if nptr == None:
            print("Heap space exceeded max limit!")
            except OutOfMemoryError("Heap space exceeded max limit!")
        }
        if self.size == MAX_SIZE:
            print("Stack overflow!")
            throw new RuntimeException("Stack overflow!")
        }
        if self.tos == None:
            self.tos = nptr
        else:
            nptr.link = self.tos
            self.tos = nptr
        self.size += 1
        print("{0} is pushed to the stack".format(val))

    def pop(self):
        if self.tos == None or self.size == 0:
            print("Stack underflow!")
            throw new RuntimeException("Stack underflow!")
        }
        val = self.tos.data
        self.tos = self.tos.link
        self.size -= 1
        print("{0} is poped from the stack".format(val))
        return val

    def display(self):
        currNode = self.tos
        StringBuilder sb = new StringBuilder("start -> ")
        while(currNode.link != null) {
            sb.append(currNode.data + " ")
            currNode = currNode.link
        }
        sb.append(currNode.data)   
        sb.append(" <- end\n")
        System.out.println(sb.toString())   


lst = StackLinkedList()
lst.push(5)
lst.push(11)
lst.push(17)
lst.push(2)
lst.push(8)
lst.push(23)
lst.display()
lst.pop()
lst.pop()
lst.display()
