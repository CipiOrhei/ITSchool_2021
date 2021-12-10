import meniu
import state_machine
"""
 Acesta este modulul principal al proiectului
"""

config_file = 'config.txt'
stare_sistem = 'Idle'



def main(stare):
    # initializam optiunea cu valoarea lui reset, care este 1
    opt = 1
    stare_noua = stare
    while opt != 0:
        # apelez functia de vizualizare de meniu
        meniu.main_meniu(stare_noua)
        # optiun de la utilizator optiunea dorita
        opt = int(input("Alege optiunea: "))
        # pentru starea si optiunea aleasa apelam functionalitatea de riguare
        stare_noua = state_machine.main_state_machine_function(stare_noua, opt)

    return stare_noua


if __name__ == '__main__':
    # citesc starea initiala la pornirea programului
    file = open(config_file, 'r')
    stare = file.read()
    file.close()
    # intru in functia main
    stare_noua = main(stare)
    # scriem starea noua in fisier
    file = open(config_file, 'w')
    stare = file.write(stare_noua)
    file.close()