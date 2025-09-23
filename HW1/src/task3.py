import sys
sys.setrecursionlimit(2000)
def numberCheck(a):
    if(a == 0):
        return "number is equal to 0"
    elif(a > 0):
        return "number is positve"
    else:
        return "number is negative"
def printprimes():
    prime = [1,3,5,7,11,13,17,19,23,29]
    for i in range(10):
        print(prime[i])
    return(prime)
def sum100():
    j = 1
    a = 0
    while(j < 101):
        a = a + j
        j+= 1
    print(a)
    return(a)
sum100()