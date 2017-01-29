private static boolean less(Comparable v, Comparable w)
{ return v.compareTo(w) < 0; }

private static void exch(Comparable[] a, int i, int j)
{
Comparable swap = a[i];
a[i] = a[j];
a[j] = swap;
}

private static boolean isSorted(Comparable[] a)
{
for (int i = 1; i < a.length; i++)
if (less(a[i], a[i-1])) return false;
return true;
}
# Returns a negative integer, zero, or positive integer
# if v is less than, equal to, or greater than w, respectively.
# Throws an exception if incompatible types (or either is null).
class Foo:
    def __init__ (self, a, b):
        self.a = a
        self.b = b

    def check(self):
        if self.__lt__():
            print("Happy")

    def __lt__ (self):
        if self.a == self.b:
            return self.b < self.b
        return self.a < self.b

    def __gt__ (self, other):
        return other.__lt__(self)

    def __eq__ (self, other):
        return self.a == other.b and self.b == other.b

    def __ne__ (self, other):
        return not self.__eq__(other)

first = Foo(8,2)
first.check()