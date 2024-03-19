class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, b):
        super().__init__(b)
        self.b = b

class C(A):
    def __init__(self, c):
        super().__init__(c)
        self.c = c

class D(B, C):
    def __init__(self, a, b, c):
        A.__init__(self, a)  
        B.__init__(self, b)  
        C.__init__(self, c) 

d = D(1, 2, 3)

print(isinstance(d, A), isinstance(d, B), isinstance(d, C)) 

print(d.a, d.b, d.c)