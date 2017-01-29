class StackofStrings:
    
    first = None
    
    class node:
        
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def isempty(self):
        if self.first == None:
            return  True
        else:
            return False
        
    def push(self,new_string):
        if self.isempty():
            self.first = self.node(new_string)
        else:
            oldfirst = self.first
            self.first = self.node(new_string)
            self.first.data = new_string
            self.first.next = oldfirst
        #print(self.first.data,self.first.next)
        
    def pop(self,remove_string):
        if isempty():
            self.first = None
        else:
            item = first.data
            first = first.next
            return item
            
stack=StackofStrings()
stack.push(8)
stack.push(9)
stack.push(11)
stack.push(12)