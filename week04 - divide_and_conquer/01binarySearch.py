#itens de k em N
valuesN = input("").split()[1:]
valuesK = input("").split()[1:]
valuesN = [int(item) for item in valuesN] #list of integers
valuesK = [int(item) for item in valuesK] #list of integers

def binarySearch(array, low, high, key):
    if(low<=high):
        middle = (high+low)//2
        if(middle>=len(array)):
            return -1
        if(key == array[middle]):
            return middle
        elif(key<array[middle]):
            return binarySearch(array, low, middle-1, key)
        else:
            return binarySearch(array, middle+1, high, key)
    else:
        return -1

def questionBinary(valuesN, valuesK):
    result = []
    for i in range(0,len(valuesK)):
        result.append(binarySearch(valuesN, 0, len(valuesN), valuesK[i]))
    return str(result).replace(",", " ", len(valuesK)-1)[1:-1]

print(questionBinary(valuesN, valuesK))



