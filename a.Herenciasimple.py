class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def traslacion(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __str__(self):
        return "X: {}; Y: {}".format(self.x, self.y)

# Ejemplo de uso
a = Punto2D(1, 2)
print("A = {}".format(a))
a.traslacion(-1, -2)
print("A = {}".format(a))

b = Punto2D(-3, 0)
b.traslacion(5, -1)
print("B = {}".format(b))

class Punto3D(Punto2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def traslacion(self, dx, dy, dz):
        super().traslacion(dx, dy)
        self.z += dz
    
    def __str__(self):
        return "X: {}; Y: {}; Z: {}".format(self.x, self.y, self.z)

# Ejemplo de uso
c = Punto3D(1, 5, -3)
print("C = {}".format(c))
c.traslacion(0, -2, 1)
print("C = {}".format(c))
