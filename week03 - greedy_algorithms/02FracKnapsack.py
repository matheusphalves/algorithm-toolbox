from functools import reduce
setItems =[]; #matrix which contains all values and weights of items
data = input("").split() # number items and capacity Weight of knapsack

def maxValue(number, weight):
    fractions = 0.
    for i in range(0, len(setItems)):
        if (weight == 0):
            break;
        if(setItems[i][1]<=weight):
            fractions += setItems[i][0]
            weight -= setItems[i][1]
        else:
            newFraction = weight/setItems[i][1]
            fractions += setItems[i][0]*newFraction
            weight -= newFraction*setItems[i][1] #fraction of weight added to get the maximum value
    return fractions


def getValues():
    while(len(setItems)<int(data[0])):
        values = input("").split()
        setItems.append((int(values[0]), float(values[1]), float(values[0])/float(values[1])))
    setItems.sort(key=lambda x:x[2], reverse=True)
#CODE EXECUTION
getValues()
value = maxValue(int(data[0]), float(data[1]))
print("{:.4f}".format(value))
