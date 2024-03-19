class Base: 
 
    def __init__(self): 
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        print(self.b) 
 
    def C(self): 
        print(self.c) 
 
class Derivada(Base): 
 
    def __init__(self): 
        self.a = "aa" 
        super().__init__() 
        self.c = "cc" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        self.b = "bb" 
        super().B() 
        print(self.b) 
 
base = Base() 
derivada = Derivada() 
 
base.A() 
derivada.A() 
print() 
base.B() 
derivada.B() 
base.C() 
derivada.C() 
derivada = base 
derivada.C() 

"""
Explicaciones de los output:
La primera a se genera porque se llama a base de A y esto hace que que se printee self a
la segunda a es engañosa porque a simple vista deberia devolver aa pero de vuelve a porqur llama a la funcion A dentro de derivada donde se recoge el self a de base y no el nuevo self a de derivada
El espacio es un simple print vacio
El b hace lo mismo que base A pero llamando a B
El primer bb es su derivada que claramente se define especificamente en la funcion B de la clase derivada
El segundo bb es porque se llama al super que es como si hubieras vuelto a ahcer el proceso de derivada de B
La primera c es simplemente base C como en a y b anteriormente
La cc es llamada por la derivada y y aque no tiene una uncion especifica dentro de derivada busca ese valor en el self del init
La ultima c solo tiene ese valor porque a derivada le da todos los valores de la clase base y base de c es c
"""