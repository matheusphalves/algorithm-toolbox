from functools import reduce
listFib = []; #list with fib results
listFib.append(0)  # n=0
listFib.append(1)  # n=1

def lastDigitSum(n):
    sizeList = len(listFib) #
    if n<sizeList:
        return listFib[n]
    else:
        #(sizeList-1) the last index value
        # n is the index than i need to know
        #the, i must calculate result = n - sizeList-1
        for i in range(n -(sizeList-1)): #I don't calculate all 'n' terms. I need to know how many terms (index) must be increased.
            listFib.append(listFib[-1] + listFib[-2]) #actual term is sum of previous two terms in the sequence
    sum = reduce((lambda x,y: x+y), listFib)
    return str(sum)[-1] #last index of list

number = int(input(""))
print(lastDigitSum(number))

