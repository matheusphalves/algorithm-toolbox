tupleCoins = (10, 5, 1)
def coins(number):
    index = 0;
    counter = 0;
    aux = 0
    while(counter<number):
        if(counter + tupleCoins[index]<=number):
            counter += tupleCoins[index]
            aux += 1
        else:
            index += 1

    return aux


number = int(input(""))
print(coins(number))
