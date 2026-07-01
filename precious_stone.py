class PreciousStone:
    stonesList = []
    maxStonesHeld = 5

    def __init__(self, stone):
        self.stone = stone
        PreciousStone.stonesList.append(self.stone)
        if len(PreciousStone.stonesList) > PreciousStone.maxStonesHeld:
            del PreciousStone.stonesList[0]

    @staticmethod
    def printStonesList():
        finalStonesList = ", ".join(PreciousStone.stonesList)
        print(finalStonesList)


preciousStoneOne = PreciousStone("Diamond")
preciousStoneTwo = PreciousStone("Amber")
preciousStoneThree = PreciousStone("Ruby")
preciousStoneFour = PreciousStone("Sapphire")
preciousStoneFive = PreciousStone("Onyx")
preciousStoneFive.printStonesList()
preciousStoneSix = PreciousStone("Kyanite")
preciousStoneSix.printStonesList()
preciousStoneSeven = PreciousStone("Magnetite")
preciousStoneSeven.printStonesList()
preciousStoneEight = PreciousStone("Uraninite")
preciousStoneEight.printStonesList()
