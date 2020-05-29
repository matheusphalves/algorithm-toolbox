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
            listFib.append((listFib[-1] + listFib[-2])) #actual term is sum of previous two terms in the sequence
    return listFib[-1] #last index of list


def pisanoPeriod(m): #returns the periodic every fib(n) on mod(m)
    modMValues = [0,1,1];
    counter = 3;
    if m>2:
        while(True):
            modMValues.append(fibList(counter)%m)
            if(modMValues[-2]==0 and modMValues[-1]==1): #the period starts with 0 1
                break;
            counter +=1
    else:
        return counter;
    return counter-1;

def fibNumberAgain(n, m):
    multiple = int(n%pisanoPeriod(m))
    if(multiple!=0):
        fib = multiple
    else:
        fib = n;
    return fibList(fib)%m;

numbers = input("").split()
print(fibNumberAgain(int(numbers[0]), int(numbers[1])))
