# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase
import math

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


# ------------------- fast io --------------------
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(a, b): return a * b // gcd(a, b)


def is_prime(n):
    if (n <= 1):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

# ------------------- write code from here --------------------
#1150B
def solve(n,l):
    c=0
    #c=[(0,0),(n,n),(0,n),(n,0)]
    for i in range(n-2):
        for j in range(n-1):
            if l[i][j]==".":
                if l[i+1][j-1]==l[i][j] and l[i+1][j]==l[i][j] and l[i+1][j+1]==l[i][j] and l[i+2][j]==l[i][j]:
                    l[i][j]="#";l[i+1][j-1]="#";l[i+1][j]="#";l[i+1][j+1]="#";l[i+2][j]="#"
                else:return "NO"
    for i in l:
        c+=i.count(".")
    if c==0:return "YES"
    else:return "NO"

m=int(input())
l=[]
for i in range(m):
    #l+=list(input())
    l.append(list(input()))
print(solve(m,l))
#print(l)
