#Slow Fibonacci algorithm
def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

listFib = []; #list with fib results
listFib.append(0)  # n=0
listFib.append(1)  # n=1

def fibList(n):
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

print("Slow Fibonacci -->")
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(10))

print("Fast Fibonacci -->")
print(fibList(0))
print(fibList(1))
print(fibList(2))
print(fibList(331))
print(fibList(99))
#print(fibList(4))
#print(fibList(10))
#print(fibList(3))

#print(listFib)

