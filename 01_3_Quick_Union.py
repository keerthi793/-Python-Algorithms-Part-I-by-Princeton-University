class QuickUnionUF:
        
    U_id = []

    def __init__(self,N):
        self.N = N
        for i in range(0,self.N):
            self.U_id.append(i)
        
    def root(self,i):
        self.i = i
        while self.i != self.U_id[i]:
            self.i = self.U_id[i]
        return self.i
        
    def connected(self,p,q):
        self.p = p
        self.q = q
        if self.root(self.p) == self.root(self.q):
            return True
        else:
            return False

    def union(self,p,q):
        self.p = p
        self.q = q
        i = self.root(self.p)
        j = self.root(self.q)
        self.U_id[i] = j
        
        
check = QuickUnionUF(10)

print("Before connecting:\n",check.U_id)

# Connecting elements
check.union(4,3)
check.union(3,8)
check.union(6,5)
check.union(9,4)
check.union(2,1)

print("After connecting:\n",check.U_id)

# Checking whether elements are connected
print("Connection status:")
print(check.connected(9,1))
print(check.connected(2,1))