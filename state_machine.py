
def main_state_machine_function(stare, optiune):
    stare_noua = stare

    if optiune != 0:
        if optiune == 1:
            print('Sistemul s-a resetat')
            stare_noua = 'Idle'
        else:
            if stare == 'Idle':
                if optiune == 2:
                    # TODO Sa chemam o functie care sterge documentele/resursele generate de la ultima saptamana
                    stare_noua = 'Licitatie'
                    print('Licitatia a inceput. Firmele se pot inscrie!')
                else:
                    print('ERROR!', 'Optiunea nu este valida pentru aceasta stare')

            elif stare == 'Licitatie':
                if optiune == 2:
                    # TODO functie care gestioneaza firmele
                    stare_noua = 'Cerere'
                    print('Cererea a inceput. Necesarul de transport se poate actualiza!')
                else:
                    print('ERROR!', 'Optiunea nu este valida pentru aceasta stare')

            elif stare == 'Cerere':
                if optiune == 2:
                    # TODO functie care gestioneaza necesarul de transport
                    stare_noua = 'Procesare'
                    print('Procesare a inceput. Nu se poate modificat necesarul sau firmele inscrise!')
                else:
                    print('ERROR!', 'Optiunea nu este valida pentru aceasta stare')

            elif stare == 'Procesare':
                if optiune == 2:
                    # TODO functie care cauta cel mai rapid orar de transport
                    stare_noua = 'Finalizare'
                    print('Generam cel mai rapid orar!')
                elif optiune == 3:
                    # TODO functie care cauta cel mai rapid orar de transport
                    stare_noua = 'Finalizare'
                    print('Generam cel mai ieftin orar!')
                else:
                    print('ERROR!', 'Optiunea nu este valida pentru aceasta stare')

            elif stare == 'Finalizare':
                if optiune == 2:
                    # TODO functie care genereaza orarul in format excel
                    print('Generam orar in format excel!')
                elif optiune == 3:
                    # TODO functie care genereaza orarul in format word
                    print('Generam orar in format word!')
                elif optiune == 4:
                    # TODO functie care genereaza factura
                    print('Generam facturile de riguare!')
                    stare_noua = 'Idle'
                else:
                    print('ERROR!', 'Optiunea nu este valida pentru aceasta stare')
    else:
        print('Sistemul se inchide!')

    return stare_noua