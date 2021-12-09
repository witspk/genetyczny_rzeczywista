from populacja import Populacja, ESelection, ECross, EMutation


def runner(wielkosc_populacji=1000,
           liczba_epok=100,
           rodzaj_selekcji=ESelection.BEST,
           parametr_selekcji=0.10,
           rodzaj_krzyzowania=ECross.ARITHMETIC,
           p_krzyzowania=0.8,
           rodzaj_mutacji=EMutation.UNIFORM,
           p_mutacji=0.5,
           liczba_elitarnych=1):
    epoki = []
    for x in range(liczba_epok):
        if x == 0:
            epoki.append(Populacja(wielkosc_populacji))
        else:
            epoki.append(epoki[x - 1]
                         .nowa_epoka(rodzaj_selekcji,
                                     parametr_selekcji,
                                     rodzaj_krzyzowania,
                                     p_krzyzowania,
                                     rodzaj_mutacji,
                                     p_mutacji,
                                     liczba_elitarnych))
    print("Wiekość populacji pierwszej epoki:"+str(len(epoki[0].population)))
    # epoki[0].print()
    print("Wiekość populacji ostatniej epoki:"+str(len(epoki[liczba_epok - 1].population)))
    # epoki[liczba_epok - 1].print()
    epoki[liczba_epok - 1].best_number(1).print()
