#knows as Eclidean Algorithm
# d divides a and b if and only if it divides a' and b
# then, gdc(a,b) = gdc(a', b) = gdc(b, a') ... until case base b==0, return a
def euclideanGcd(a,b):
    if(b==0):
        return a
    else:
        return euclideanGcd(b, int(a%b))

numbers = input("").split()
print(euclideanGcd(int(numbers[0]), int(numbers[1])))