class UF:
    def __init__(self,N):
        self.N = N
    
    def union(self,p,q):
        pass
    
    def connected(self,p,q):
        pass
    
    def find(self,p):
        pass
    
    def count(self,c):
        pass

def main():
    N = int(input().strip())
    uf = UF(N)
    while ( N != ''):
        p=int(input().strip())
        q=int(input().strip())
        if (connected(self,p,q) == 'False'):
            uf.union(p,q)
            print(p+' is conncected '+q)