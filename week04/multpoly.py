#Naive algorithm
def multiPoly(A, B, n):
    product = []
    for i in range(0, 2*n-1): #initializing with zeros
        product.append(0)
    for i in range(0, n):
        for j in range(0, n):
            product[i+j] += A[i]*B[j]
    return product
# O(n²)

print(multiPoly((3,2,5),(5,1,2),3))