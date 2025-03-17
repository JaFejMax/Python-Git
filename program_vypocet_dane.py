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
        "bulding site": 9,
        "forrest": 0.35,
        "garden": 2
    }
    def __init__(self, locality, estate_type, area):
        super.__init__(locality)
        self.estate_type = estate_type
        self.area = area
#area v metrech ctverecnich
    def calculate_tax_estate(self):
        if self.estate_type not in self.Estate_types_coef:
            return print("Neplatný typ pozemku.")
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
    def calculate_tax_residence(self):
        tax_residence = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
            tax_residence = 2
        return math.ceil(tax_residence)

