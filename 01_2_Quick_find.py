class QuickFindUF:
    
    UF_id = []

    def __init__(self,N):
        self.N = N
        for i in range(0,self.N):
            self.UF_id.append(i)
          
    def union(self,p,q):
        self.p = p
        self.q = q
        pid = self.UF_id[self.p]
        qid = self.UF_id[self.q]
        for i in range(0,len(self.UF_id)):
            if self.UF_id[i] == pid:
                self.UF_id[i] = qid
    
    def connected(self,p,q):
        self.p = p
        self.q = q
        if self.UF_id[self.p] == self.UF_id[self.q]:
            return True
        else:
            return False
            

check = QuickFindUF(10)

# Connecting elements
check.union(4,3)
check.union(3,8)
check.union(6,5)
check.union(9,4)
check.union(2,1)

print("After connecting:\n",check.UF_id)

# Checking whether elements are connected
print("Connection status:")
print(check.connected(4,8))
print(check.connected(1,9))