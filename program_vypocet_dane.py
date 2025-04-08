import math
#trida pro katastr/obec
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient
#name je pro nazev katastru/obce; locality_coefficient je specificky koeficient pro katastr

#trida pro nemovitost
class Property:
    def __init__(self, locality):
        self.locality = locality
#locality má být objektem třídy Locality

class Estate(Property):
    Estate_types_coef = {
        "land": 0.85,
        "building site": 9,
        "forest": 0.35,
        "garden": 2
    }
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
#area v metrech ctverecnich
    def calculate_tax(self):
        if self.estate_type not in self.Estate_types_coef:
            print("Neplatný typ pozemku.")  # Nejprve vypíše chybovou zprávu
            return 0
        tax_estate = self.area * self.Estate_types_coef[self.estate_type] * self.locality.locality_coefficient
        return math.ceil(tax_estate)
#vypocet dane, ktera spocita dan pro pozemek a vrati cele cislo

#vytvoreni tridy Residence, která reprezentuje stavbu
#area jsou metry ctverecni stavby, commercial urcuje podnikani/osobni ucel stavby
class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        tax_residence = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
            tax_residence = 2*tax_residence
        return math.ceil(tax_residence)

# Testování lokalit
manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

# Testované nemovitosti
# estate1 = Estate(manetin, "cottage", 900)  # neplatný objekt pozemek v Manětíně
estate1 = Estate(manetin, "land", 900)
residence1 = Residence(manetin, 120)  # Dům v Manětíně
office = Residence(brno, 90, commercial=True)  # Kancelář v Brně

# Výstupy
print(f"Daň z pozemku: {estate1.calculate_tax()} Kč")  # Očekávaný výstup: 612
print(f"Daň z domu: {residence1.calculate_tax()} Kč")  # Očekávaný výstup: 1440
print(f"Daň z kanceláře: {office.calculate_tax()} Kč")  # Očekávaný výstup: 8100
