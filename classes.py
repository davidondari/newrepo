class Manga:
    def __init__(self, name, year, popularity, hero):
        self.name = name
        self.year = year
        self.popularity = popularity
        self.hero = hero
        self.compress = self.name, self.hero


m1 = Manga("onepiece", 1998, 0.9, "monkey-d-ruffy")

m2 = Manga("bleach", 1998, 0.8, "i_dont_knw")

m3 = Manga("naruto", 1998, 0.5, "ehhh")

print(m1.name)
print(m1.compress)
