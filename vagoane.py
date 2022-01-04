
class Vagoane:

    def __init__(self,new_nume,new_tip,new_cantitate):
        self.nume = new_nume
        self.tip = new_tip
        self.cantitate = new_cantitate

    def get_nume(self):
        return self.nume

    def get_tip(self):
        return self.tip

    def get_cantitate(self):
        return self.cantitate

    def afisare(self):
        print("Detaliile vagoanelor: ")
        print(f"Nume vagon: {self.get_nume()}")
        print(f"Tip marfa: {self.get_tip()}")
        print(f"Cantitate: {self.get_cantitate()}")

if __name__ == "__main__":
    vag_1 = Vagoane(new_nume="Model X12",new_tip="Lemn/Busteni/Fier",new_cantitate=2)


    vag_1.afisare()
