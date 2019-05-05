class Node:
    def __init__(self):
        self.data = 0
        self.link = null

    def __init__(self,data,lnk):
        self.data = data
        self.link = lnk

class SinglyLinkedList:
    def __init__(self):
        self.size = 0
        self.start = self.end = None

    def insert_at_beg(self,val):
        nptr = Node(val,None)
        if self.start == None:
            self.start = self.end = nptr
        else:
            nptr.link = self.start
            self.start = nptr
        self.size += 1

    def append(self,val):
        nptr = Node(val,None)
        if self.start == None:
            self.start = self.end = nptr
        else:
            self.end.link = nptr
            self.end = nptr
        self.size += 1

    def insert_at_pos(self,pos,val):
        nptr = Node(val,None)
        if pos > self.size:
            print("Insertion is not possible. Insert position {0} is more than size {1} of linked list".format(pos,size))
            return
        elif pos == 1:
            insert_at_beg(val)
            return
        curr_node = self.start
        for i in range(1, self.size + 1):
            if i == pos-1:
                nptr.link = curr_node.link
                curr_node.link = nptr
                break
            curr_node = curr_node.link
        self.size += 1

    def display(self):
        print("start ->",end = " ")
        curr_node = self.start
        while curr_node != None:
            print(curr_node.data,end = " ")
            curr_node = curr_node.link
        print("<- end")

    def get(self,pos):
        ret_val = -1
        if self.size == 0:
            print("List underflow!")
            return ret_val
        else:
            if pos < 1:
                print("My list index starts from 1");
                return ret_val
            elif pos > self.size:
                print("List doesn't contain so many items");
                return ret_val
            curr_node = self.start
            for i in range(1,self.size+1):
                if i == pos:
                    ret_val = curr_node.data
                    break
                curr_node = curr_node.link
        return ret_val
