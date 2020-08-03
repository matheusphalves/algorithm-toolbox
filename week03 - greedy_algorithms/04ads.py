slotNumber = int(input(""))
sequence1 = input("").split() #pay for click
sequence2 = input("").split()#estimated number of clicks

sequence1 = [int(x) for x in sequence1]
sequence2 = [int(x) for x in sequence2]
#create pair (ai, bi) such that maximized their product

def adsRevenue(slotNumber,sequence1, sequence2):
    sequence1.sort()
    sequence2.sort()
    product = 0
    for i in range(0, slotNumber):
        product += int(sequence1[i]*sequence2[i])
    return product

#START PROGRAM
print(adsRevenue(slotNumber, sequence1, sequence2))
