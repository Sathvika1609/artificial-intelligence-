class region:
    def _init_(self, rName, rColor):
        self.rName = rName  # region name
        self.rColor = rColor  # region color
        self.adjecentRegions = []  # list to store objects of Adjacent region
    def setAdjacentR(self, adjecentRegions):
        self.adjecentRegions = adjecentRegions  # set objects no. Adjacent regions
# print colors of all regions
def printState():
    print("WA  color: ", WA.rColor)
    print("NT color: ", NT.rColor)
    print("SA color: ", SA.rColor)
    print("Q color: ", Q.rColor)
    print("NSW color: ", NSW.rColor)
    print("V color: ", V.rColor)
    print("T : ", T.rColor)
# valivate colour entered by user
def validateInput(color):
    # color list
    colors = ['Red', 'Green',  'Blue']
    # check if user color input is in list of required colors
    if color in colors:
        return True
    else:
        print("Invalid color input")
        return False
    # validate user input color with Adjacent region colors
def validateColor(region, color):
    # get list of colors of all adjecent regions
    colors_of_Adjacent_r = [region.rColor for region in region.adjecentRegions]
    # check if user input color is present in list of Adjacent region color
    if color in colors_of_Adjacent_r:
        print("one of the Adjacent region has same color!!")
        print("!!!!! GAME OVER !!!!!")
        return False
    else:
        return True
# if user lost the game clear colors set by him. by painting all regions with default white color
def clearMemory():
    WA.rColor = 'white'
    NT.rColor = 'white'
    SA.rColor = 'white'
    Q.rColor = 'white'
    NSW.rColor = 'white'
    V.rColor = 'white'
    T.rColor = 'white'
# DRIVER CODE
# number of regions
N = 7
# object of regions
# Initially lets paint all regions with white color
WA = region('WA', 'White')
NT = region('NT', 'White')
SA = region('SA', 'White')
Q = region('Q', 'White')
NSW = region('NSW', 'White')
V = region('V', 'White')
T = region('T', 'White')
# set adjacent regions all regions by passing list of Adjacent regions object
WA.setAdjacentR([NT,SA])
NT.setAdjacentR([WA,SA,Q])
SA.setAdjacentR([WA,NT,Q,NSW,V])
Q.setAdjacentR([NT,SA,NSW])
NSW.setAdjacentR([V,SA,Q])
V.setAdjacentR([SA, NSW])
T.setAdjacentR([])
while (True):
    print("===================NEW GAME==================")
    print("Red, Green, Blue")
    c1 = input("Enter color for Western Australia: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c1)):
        # color region with color entered by user
        WA.rColor = c1
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c2 = input("Enter color for Northern Territory:")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c2) and validateColor(NT, c2)):
        # color region with color entered by user
        NT.rColor = c2
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c3 = input("Enter color for South Australia: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c3) and validateColor(SA, c3)):
        # color region with color entered by user
        SA.rColor = c3
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c4 = input("Enter color for Queensland: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c4) and validateColor(Q, c4)):
        # color region with color entered by user
        Q.rColor = c4
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c5 = input("Enter color for New South Wales: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c5) and validateColor(NSW, c5)):
        # color region with color entered by user
        NSW.rColor = c5
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
