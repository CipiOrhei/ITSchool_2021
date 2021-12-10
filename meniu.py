"""
In acest modul ne ocupam doar de vizualizarea meniului.
Acesta se poate extinde.
"""

"""
starea Idle: sistemul este in asteptare
            Conditii: se pot aduga firme si modifica necesarul
starea Licitatie: sistemul sterge datele vechi si astepta date noi
starea Cerere: Firmele sunt procesate si nu se mai pot adauga firme noi
starea Procesare: Necesarul nu mai poate fi modificat
starea Finalizare - Sistemul creeaza orarul necesar

"""

text_meniu_stare_0 = """
0. Iesire
1. Reset
2. Porniti inscrierea firmelor
"""

text_meniu_stare_1 = """
0. Iesire
1. Reset
2. Oprire si prelucarea firmelor adaugate
"""

text_meniu_stare_2 = """
0. Iesire
1. Reset
2. Prelucarea transporturilor necesare
"""

text_meniu_stare_3 = """
0. Iesire
1. Reset
2. Generare cel mai rapid orar
3. Generare cel mai ieftin orar
"""

text_meniu_stare_4 = """
0. Iesire
1. Reset
2. Generare orar excel
3. Generare orar word
4. Generare factura
"""

def main_meniu(stare):
    if stare == 'Idle':
        print(text_meniu_stare_0)
    elif stare == 'Licitatie':
        print(text_meniu_stare_1)
    elif stare == 'Cerere':
        print(text_meniu_stare_2)
    elif stare == 'Procesare':
        print(text_meniu_stare_3)
    elif stare == 'Finalizare':
        print(text_meniu_stare_4)
    else:
        print('ERROR!','Nu exista starea aceasta')
