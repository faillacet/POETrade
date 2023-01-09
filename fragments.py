class FragSet:
    def __init__(self, names, bulkPriceDiv):
        self.fragmentNames = names
        self.divinePrice = None
        self.totalPrice = None
        self.bulkPriceDiv = bulkPriceDiv
        self.bulkPriceChaos = None
        self.profit = None

    def calculateAll(self, fragmentData, currencyData):
        # Grab Divine Price
        for item in currencyData:
            if (item['currencyTypeName'] == 'Divine Orb'):
                self.divinePrice = item['chaosEquivalent']
                break

        #
        self.calcTotalPrice(fragmentData)
        self.calcBulkChaos()
        self.calcEstimatedProfit()
    

    def calcTotalPrice(self, fragmentData):
        totalPrice = 0
        for item in fragmentData:
            if (item['currencyTypeName'] in self.fragmentNames):
                #print(item['currencyTypeName'] + ": " + str(item['chaosEquivalent']))
                totalPrice = totalPrice + item['chaosEquivalent']

        # Speical Case for Maven Set
        if (self.fragmentNames[0] != 'Crescent Splinter'):
            self.totalPrice = totalPrice
        else:
            self.totalPrice = totalPrice * 10
        return

    def calcBulkChaos(self):
        self.bulkPriceChaos = self.bulkPriceDiv * self.divinePrice

    def calcEstimatedProfit(self):
        self.profit = self.bulkPriceChaos - self.totalPrice


# DEFINE ALL FRAG SETS
allSets = { 'Elder': FragSet(['Fragment of Purification', 'Fragment of Constriction', 'Fragment of Enslavement', 'Fragment of Eradication'], .5),
            'Shaper': FragSet(['Fragment of the Hydra', 'Fragment of the Chimera', 'Fragment of the Phoenix', 'Fragment of the Minotaur'], 1/3),
            'Uber Elder': FragSet(['Fragment of Knowledge', 'Fragment of Shape', 'Fragment of Terror', 'Fragment of Emptiness'], 1.5),
            'Sirus': FragSet(['Veritania\'s Crest', 'Drox\'s Crest', 'Al-Hezmin\'s Crest', 'Baran\'s Crest'], .33),
            'Maven': FragSet(['Crescent Splinter'], .9)
            }