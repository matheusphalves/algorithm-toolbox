from functools import reduce
listFib = []; #list with fib results
listFib.append(0)  # n=0
listFib.append(1)  # n=1

def lastDigitSumRange(n, m):
    sizeList = len(listFib)
    sum =0
    if m<sizeList:
        return listFib[m]
    else:
        for i in range(m -(sizeList-1)): #I don't calculate all 'n' terms. I need to know how many terms (index) must be increased.
            listFib.append((listFib[-1] + listFib[-2])%10) #actual term is sum of previous two terms in the sequence


    newList = list(filter(lambda x: (listFib.index(x)>=n and listFib.index(x)<=m), listFib))
    sum = reduce(lambda x,y: x+y, newList)
    return sum%10 #last index of list


number = input("").split()
print(lastDigitSumRange(int(number[0]), int(number[1])))