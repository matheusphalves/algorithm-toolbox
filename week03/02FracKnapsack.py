from functools import reduce
setItems =[]; #matrix which contains all values and weights of items
data = input("").split() # number items and capacity Weight of knapsack

def maxValue(number, weight):
    fractions = []
    for i in range(number-1, -1, -1):
        if (weight <= 0):
            break;
        if(setItems[i][1]<=weight):
            fractions.append(setItems[i][0]) #100% values
            weight -= setItems[i][1]
        else:
            newFraction = weight/setItems[i][1]
            fractions.append(setItems[i][0]*newFraction)
            weight -= newFraction*setItems[i][0] #fraction of weight added to get the maximum value

    return float(reduce(lambda x, y: x+y, fractions))


def getValues():
    while(len(setItems)<int(data[0])):
        values = input("").split()
        setItems.append((int(values[0]), float(values[1]), float(values[0])/float(values[1])))
    setItems.sort(key=lambda x:x[2])
#CODE EXECUTION
getValues()
value = maxValue(int(data[0]), float(data[1]))
print("{:.4f}".format(round(value, 4)))
