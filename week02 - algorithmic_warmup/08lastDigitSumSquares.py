from functools import reduce
listFib = [0,1]; #list with fib results

def fibSquare(n):
    sizeList = len(listFib) #
    if n<sizeList:
        return listFib[n]
    else:
        #(sizeList-1) the last index value
        # n is the index than i need to know
        #the, i must calculate result = n - sizeList-1
        for i in range(n -(sizeList-1)): #I don't calculate all 'n' terms. I need to know how many terms (index) must be increased.
            listFib.append(((listFib[-1] + listFib[-2])%10)) #actual term is sum of previous two terms in the sequence
    return listFib[-1] #last index of list
def squareFib(n):
    fibSquare(n%60)
    filterList =  list(filter(lambda x: listFib.index(x)<=n%60, listFib))
    newList = list(map(lambda x: x*x, filterList))
    return reduce((lambda x, y: x+y), newList)%10


number = int(input(""))
print(squareFib(number))