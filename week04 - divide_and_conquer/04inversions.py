n = int(input("")) #size of list
valuesN = input("").split() #input values
valuesN = [int(item) for item in valuesN] #list of integers

def question(array):
    #tuple (array, 0), when [0] is array and [1] is inversions counter
    return mergeSort((array, 0))[1]

def mergeSort(tuple):#A cada iteração, o array é dividido em duas metades
    if(len(tuple[0])>1): #deve haver no mínimo dois elementos para dividir
        n = len(tuple[0]) // 2 #ERRO AQUI!!!
        leftList = tuple[0][0:n]
        rightList = tuple[0][n:]
        auxTuple = merge(mergeSort((leftList, tuple[1])), mergeSort((rightList, tuple[1])))
        return (auxTuple[0], auxTuple[1]) #(Array, inversions counter)
    else:
        return (tuple[0] , 0) #retornando único elemento

def merge(tuple1, tuple2):
    auxArray = []
    inversions = 0
    #durante a recursão, listas maiores que 1 estarão ordenadas. Condição para que o algoritmo funcione corretamente.
    #print(f'Arrays: {tuple1[0]} + {tuple2[0]}')
    while(tuple1[0]  and tuple2[0]): #Encontramos os elementos minimos em cada subsequencia e então os comparamos
        if(tuple1[0][0]<=tuple2[0][0]):
            auxArray.append(tuple1[0][0])
            tuple1[0].pop(0)
        else:
            auxArray.append(tuple2[0][0])
            tuple2[0].pop(0)
            inversions += len(tuple1[0])
    #print(inversions)

    auxArray += tuple1[0] or tuple2[0]
    return (auxArray, tuple1[1] + tuple2[1] + inversions)


print(question(valuesN))