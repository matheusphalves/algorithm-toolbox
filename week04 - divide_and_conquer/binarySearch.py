def binarySearch(array, low, high, key):
    if(low<=high):
        middle = (high+low)//2
        if(key == array[middle]):
            return middle
        elif(key<array[middle]):
            return binarySearch(array, low, middle-1, key)
        else:
            return binarySearch(array, middle+1, high, key)
    else:
        return -1

#lista = [3,5,8,10,12,15,18,20,20,50,60]
lista = [1, 5, 8, 12, 13]

print(binarySearch(lista, 0,5,1))
print(binarySearch(lista, 0,5,5))
print(binarySearch(lista, 0,5,8))
print(binarySearch(lista, 0,5,12))
print(binarySearch(lista, 0,5,13))
