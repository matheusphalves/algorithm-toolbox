#bubble sort

#insertion sort


#selection sort
def selectionSort(arrayList):
    size = len(arrayList)

    if(size>1):
        for i in range(1, size):
            minIndex = i
            for j in range(i+1, size):
                if(arrayList[j]<arrayList[minIndex]):
                    swap(arrayList, j, i)

    return arrayList #there is one element!

def swap(arrayList, indexA, indexB):
    aux = arrayList[indexA]
    arrayList[indexA] = arrayList[indexB]
    arrayList[indexB] = aux


list = [2, 4, 8, 5, 2]

print(selectionSort(list))
#merge sort


#quick sort