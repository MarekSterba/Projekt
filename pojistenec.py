class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, mobil):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.mobil = mobil

    def __str__(self):
        return f'{self.jmeno}   {self.prijmeni}   {self.vek}   {self.mobil}'
    
seznam_pojistencu = [
    Pojistenec("Marek", "Sterba", 39, 1234),
    Pojistenec("Karel","Novak", 28, 4321),
    Pojistenec("Josef","Skala", 35, 5678),
    Pojistenec("Michal","Novotny", 56, 8765),
    Pojistenec("Petr","Kroupa", 44, 2468),
]