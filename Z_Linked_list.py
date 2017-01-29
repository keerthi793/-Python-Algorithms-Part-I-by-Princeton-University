class node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # This function prints contents of linked list
    # starting from head
    
    def printlist(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
        
ll = LinkedList()

ll.head = node(1)
second = node(2)
third = node(3)

'''
Befor connecting 3 nodes:
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
'''


ll.head.next = second
second.next = third

'''
After connecting nodes:

ll.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
'''
# Printing the function using first object ll
ll.printlist()
