"""
Modul care gestioneaza firmele
"""
import glob
from docx import Document

LOCATIE_FOLDER_FIRME = r"c:\repos\ITSchool_2021\Documente\firme_licitatie"
LISTA_FIRME_DISPONIBILE = list()

class Firme:
    def __init__(self, nume):
        """
        Constructor pentru clasa firma
        :param nume: numele firmei
        """
        self.nume = nume
        # cream o lista cu toate locomotivele posibile
        self.lista_locomotive = list()
        self.lista_locomotive.append({'model': 'A', 'cantitate': 30, 'viteza': 100, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0})
        self.lista_locomotive.append({'model': 'B', 'cantitate': 60, 'viteza': 80, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0})
        self.lista_locomotive.append({'model': 'C', 'cantitate': 30, 'viteza': 150, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0})
        self.lista_locomotive.append({'model': 'D', 'cantitate': 50, 'viteza': 70, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0})
        self.lista_locomotive.append({'model': 'E', 'cantitate': 45, 'viteza': 75, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0})
        # cream o lista cu toate vagoanele posibile
        self.lista_vagoane = list()
        self.lista_vagoane.append({'model': 'X12', 'cantitate': 2, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Lemn', 'Busteni', 'Fier']})
        self.lista_vagoane.append({'model': 'X14', 'cantitate': 4, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Lemn', 'Busteni', 'Fier']})
        self.lista_vagoane.append({'model': 'X13', 'cantitate': 5, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Nisip', 'Cherestea', 'Piatra']})
        self.lista_vagoane.append({'model': 'X15', 'cantitate': 4, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Nisip', 'Cherestea', 'Piatra']})
        self.lista_vagoane.append({'model': 'X24', 'cantitate': 1, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Apa', 'Benzina']})
        self.lista_vagoane.append({'model': 'X23', 'cantitate': 5, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Apa', 'Benzina']})
        self.lista_vagoane.append({'model': 'X25', 'cantitate': 10, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Apa', 'Benzina']})
        self.lista_vagoane.append({'model': 'X5', 'cantitate': 1, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Pasageri']})
        self.lista_vagoane.append({'model': 'X10', 'cantitate': 5, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Pasageri']})
        self.lista_vagoane.append({'model': 'X30', 'cantitate': 10, 'unitati_disponibile': 0, 'unitati_folosite': 0, 'cost': 0, 'material': ['Pasageri']})

    def adauga_locomotiva(self, model, unitati, cost):
        for locomotiva in self.lista_locomotive:
            if model == locomotiva['model']:
                locomotiva['unitati_disponibile'] = unitati
                locomotiva['cost'] = cost
                break

    def adauga_vagon(self, model, unitati, cost):
        for vagoane in self.lista_vagoane:
            if model == vagoane['model']:
                vagoane['unitati_disponibile'] = unitati
                vagoane['cost'] = cost
                break


def citire_document_word(cale: str) -> dict:
    """
    Citeste dintr-un word format datele despre o firma
    :param cale:
    :return: Un dictionar cu datele necesare
    """
    tmp_dict = dict()
    document = Document(cale)
    for para in document.paragraphs:
        pass
        # print('TODO: cu ajutorul regex gasiti informatiile din fiecare paragraf')
        # Populam tmp_dict
        #TODO
    # exemplu:
    tmp_dict['nume'] = 'FerovTrans SRL'
    # tupla per locomotiva: (cantitate, model, cost)
    tmp_dict['Locomotive'] = [(5, 'C', 20), (2, 'B', 30)]
    # tupla per vagon: (cantitate, model, cost)
    tmp_dict['Vagoane'] = [(6, 'X30', 35), (5, 'X14', 45), (20, 'X25', 60)]

    return tmp_dict


def salvam_lista_firme_pe_hard():
    #TODO salvam lista cumva :)
    #poate txt, poate numpy
    pass


def procesare_firme_inscrise():
    # aflam toate documentele depuse de firme
    lista_fisier = glob.glob(LOCATIE_FOLDER_FIRME + '/*')
    # pentru fiecare fisier gasit procesam datele
    for file in lista_fisier:
        tmp_dict = citire_document_word(file)

        LISTA_FIRME_DISPONIBILE.append(Firme(tmp_dict['nume']))
        for element in tmp_dict['Locomotive']:
            LISTA_FIRME_DISPONIBILE[-1].adauga_locomotiva(model=element[1], unitati=element[0], cost=element[2])
        for element in tmp_dict['Vagoane']:
            LISTA_FIRME_DISPONIBILE[-1].adauga_vagon(model=element[1], unitati=element[0], cost=element[2])

    salvam_lista_firme_pe_hard()


if __name__ == '__main__':
    # firma_1 = Firme(nume='Ion')
    # print(firma_1)
    procesare_firme_inscrise()