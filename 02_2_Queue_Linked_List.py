class Queue_LinkedList:
    first = None
    last = None
    
    class node:
        
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def isempty(self):
        if self.first == None:
            return True
        else:
            return False
    
    def enqueue(self,data):
        if self.isempty():
            self.last = self.node(data)
            self.first = self.last
        else:
            oldlast = self.last
            self.last = self.node(data)
            oldlast.next = self.last
            print(oldlast.data,oldlast.next)
            print(self.last.data,self.last.next)
    
    def dequeue(self):
        if self.isempty():
            return None
        else:
            item = self.first.data 
            self.first = self.first.next
            return item
        
ql= Queue_LinkedList()
ql.enqueue(4)
ql.enqueue(5)
ql.enqueue(7)
print(ql.dequeue())
