class Locomotive:

    def __init__(self, new_nume, new_cantitate_maxima, new_viteza):
        self.nume = new_nume
        self.cantitate_maxima = new_cantitate_maxima
        self.viteza = new_viteza

    def get_nume(self):
        return self.nume

    def get_cantitate_maxima(self):
        return self.cantitate_maxima

    def get_viteza(self):
        return self.viteza

    def afisare(self):
        print("Detaliile locomotivei: ")
        print(f"Nume locomotiva: {self.get_nume()}")
        print(f"Cantitate maxima: {self.get_cantitate_maxima()}")
        print(f"Viteza: {self.get_viteza()}")


if __name__ == "__main__":
    loc_1 = Locomotive(new_nume="Model A", new_cantitate_maxima=30, new_viteza=100)

    loc_1.afisare()

