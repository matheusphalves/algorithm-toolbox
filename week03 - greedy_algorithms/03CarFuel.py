

distance = int(input("")) #distance between cities
tankDistance = int(input("")) #max car capacity with full tank
sizePoints = int(input("")) #max car capacity with full tank
points = input("").split()
listPoints = [0] + [int(x) for x in points] + [int(distance)]#list of points to refil

def minimumRefills(distance, tankFuel, points):
    fuel = tankFuel
    refil = 0
    index = 0;
    while(points[index]<distance):
        newDistance = points[index+1]-points[index]
        if(newDistance<=fuel):
            index += 1 #go to new point!
            fuel -= newDistance #decreasing fuel!
        else:
            fuel += (tankFuel - fuel) #new refil!
            if(fuel<newDistance):
                return -1 #there is no fuel enough
            refil +=1
    return refil


print(minimumRefills(distance, tankDistance, listPoints))