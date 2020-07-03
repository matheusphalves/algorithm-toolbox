def binarySearch(array, low, high, key):
    if(high<low):
        return low-1
    middle = low + (high-low)//2
    if(key == array[middle]):
        return middle
    elif(key<array[middle]):
        return binarySearch(array, low, middle-1, key)
    else:
        return binarySearch(array, middle+1, high, key)

lista = [3,5,8,10,12,15,18,20,20,50,60]

print(binarySearch(lista, 1,11,3))