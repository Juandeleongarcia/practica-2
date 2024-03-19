class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion

class ParedCortina(Pared):
    def __init__(self, orientacion, superficie_acristalada):
        super().__init__(orientacion)
        self.superficie_acristalada = superficie_acristalada

class Ventana:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.superficie = superficie
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.proteccion = proteccion

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_acristalada(self):
        superficie_total = 0
        for pared in self.paredes:
            if isinstance(pared, ParedCortina):
                superficie_total += pared.superficie_acristalada
            else:
                superficie_total += sum(ventana.superficie for ventana in self.ventanas_en_pared(pared))
        return superficie_total

    def ventanas_en_pared(self, pared):
        return [ventana for ventana in self.ventanas if ventana.pared == pared]

pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")

pared_cortina_sur = ParedCortina("SUR", 10)

ventana_norte = Ventana(pared_norte, 0.5, "Persiana")
ventana_oeste = Ventana(pared_oeste, 1, "Estor")
ventana_sur = Ventana(pared_sur, 2, "Cortina")
ventana_este = Ventana(pared_este, 1, "Persiana")

casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
casa.ventanas = [ventana_norte, ventana_oeste, ventana_sur, ventana_este]

print(casa.superficie_acristalada())