import random

class Penezenka():
    def __init__(self, jmeno: str, kreditniKarta: str, zustatek: int):
        self.__kreditniKarta = kreditniKarta
        self.jmeno = jmeno
        self.zustatek = zustatek

    def vybratPenize(self, castka: int):
        if self.zustatek >= castka:
            self.zustatek -= castka
            return True
        return False

    def vlozitPenize(self, castka: int):
        self.zustatek += castka
        return True



class Sazka():
    def __init__(self, castka):
        self.castka = castka

    def nastavitSazku(self, nova_sazka: int):
        self.nova_sazka = nova_sazka
        return self.castka
    

class Hrac():
    def __init__(self, vek: int, jmeno: str, zustatek: int):
        self.vek = vek
        self.jmeno = jmeno
        self.penezenka = Penezenka(jmeno, "1234-5678-8765-4321", zustatek)
        self.aktualni_sazka = 0

    def nastavitSazku(self, sazka: int):
        if self.vek < 18:
            return False
        if sazka > 0 and self.penezenka.zustatek >= sazka:
            self.aktualniSazka = sazka
            return True
        return False


class VysledekHry:
    def __init__(self, jackpot: int, vyhra: bool):
        self.jackpot = jackpot
        self.vyhra = vyhra

    def ziskatVyhru(self):
        if self.vyhra:
            return self.jackpot
        else:
            return 0

    def Jackpot(self):
        return self.jackpot > 0
    


class HerniAutomat():
    def __init__(self, nazev, vyrobce, jackpot, minSazka, maxSazka):
        self.nazev = nazev
        self.vyrobce = vyrobce
        self.jackpot = jackpot
        self.minSazka = minSazka
        self.maxSazka = maxSazka

    symboly = ["🍒", "🍋", "🍉", "⭐", "🔔", "🍇"]

    def vlozitPenize(self, castka: int):
        return castka
    
    def toc(self):
        vysledek = []
        for valec in range(9):
            symbol = random.choice(self.symboly)
            vysledek.append(symbol)
        return vysledek
    
    def vyhodnot(self, sazka: Sazka, vysledek):
        vyhra = 0
        if len(set(vysledek)) == 1: # mnozina 3 stejnych symbolu
            vyhra = sazka.castka * 3
            if vyhra >= self.jackpot:
                jackpot_hodnota = self.jackpot
            else:
                jackpot_hodnota = 0
                vyhra_existuje = vyhra > 0
        return VysledekHry(jackpot_hodnota, vyhra_existuje)
    

if __name__ == '__main__':
    pass