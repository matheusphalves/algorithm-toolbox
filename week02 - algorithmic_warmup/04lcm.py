#Last common multiple

def lcf(a,b):
    result =1;
    counter = 1;
    if(a<b):
        shorter = a;
    else:
        shorter = b;
    while(result%a!=0 or result%b!=0):
        result = shorter*counter
        counter += 1
    return result;


numbers = input("").split()
print(lcf(int(numbers[0]), int(numbers[1])))