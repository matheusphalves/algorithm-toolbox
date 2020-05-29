from functools import reduce
listFib = []; #list with fib results
listFib.append(0)  # n=0
listFib.append(1)  # n=1

def fib(n):
    sizeList = len(listFib) #
    if n<sizeList:
        return listFib[n]
    else:
        #(sizeList-1) the last index value
        # n is the index than i need to know
        #the, i must calculate result = n - sizeList-1
        for i in range(n -(sizeList-1)): #I don't calculate all 'n' terms. I need to know how many terms (index) must be increased.
            listFib.append(listFib[-1] + listFib[-2]) #actual term is sum of previous two terms in the sequence
    return listFib[-1] #last index of list
def squareFib(n):
    sum = 0;
    while(n>=2):
        actual = (fib(n-1) + fib(n-2))*(fib(n-1) + fib(n-2))
        sum += actual
        n -=1;
    return (sum+1)%10


number = int(input(""))
print(squareFib(number))