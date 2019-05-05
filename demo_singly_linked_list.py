from singly_linked_list import SinglyLinkedList

t = int(input("Enter number of test cases:"))
for i in range(0,t):
    n = int(input("Enter number of items to input:"))
    s = input("Enter items (0 => insert at begining, -1 => append):")
    idx = int(input("Enter the index of the item to fetch (Index starts from 1): "))
    ss = s.strip().split()
    ns = []
    for x in ss:
        ns.append(int(x))
        lst = SinglyLinkedList()
    for j in range(0,n*2,2):
        if ns[j] == 0:
            lst.insert_at_beg(ns[j+1])
        elif ns[j] == -1:
            lst.append(ns[j+1])
        else:
            lst.insert_at_pos(ns[j],ns[j+1])
    lst.display()
    print("The item at index {0} is {1}".format(idx,lst.get(idx)))
