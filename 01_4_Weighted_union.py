class UF:
    """An implementation of union find data structure.
    It uses weighted quick union by rank with path compression.
    """

    def __init__(self, N):
        """Initialize an empty union find object with N items.

        Args:
            N: Number of items in the union find object.
        """

        self._id = list(range(N))
        self._count = N
        self._rank = [0] * N
        print("Initial tree ",self._id)
        print("Initial weight ",self._rank)
    def find(self, p):
        """Find the set identifier for the item p."""

        id = self._id
        while p != id[p]:
            #p = id[p] = id[id[p]]   # Path compression using halving.
            p = id[p]
        return p

    def count(self):
        """Return the number of items."""

        return self._count

    def connected(self, p, q):
        """Check if the items p and q are on the same set or not."""

        return self.find(p) == self.find(q)

    def union(self, p, q):
        """Combine sets containing p and q into a single set."""

        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        self._count -= 1
        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

check=UF(10)
check.union(4,3)
check.union(3,8)
check.union(6,5)
check.union(9,4)
check.union(2,1)
check.union(5,0)
check.union(7,2)
check.union(6,1)
check.union(7,3)
print("Final tree ",check._id)
print("Final weight ",check._rank)