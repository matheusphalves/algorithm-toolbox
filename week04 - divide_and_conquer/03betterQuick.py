lenNumber = int(input(""))
itens = input("").split()
itens = [int(x) for x in itens]

def partition(array, left, right, pivot):
    i = left
    while i <= right:      #caso i > right, todos elementos são maiores que o pivô
        if array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[right] = array[right], array[i]
            right -= 1
        else:
            i += 1
           
    return left, right      #intervalo entre elementos repetidos do pivô

def quickSort(array, left, right):  
    if left >= right:
        return
    else:
        pivot = array[left]#pivô escolhido: Elementos à esquerda menores e à direita maiores
        kLeft, kRight = partition(array, left, right, pivot)
        quickSort(array, left, kLeft-1)#metades são enviadas para ordenação
        quickSort(array, kRight+1, right) 
    return array
    

#START PROGRAM
listFinal = quickSort(itens, 0, len(itens)-1)
for x in listFinal:
        print(x, end=' ')