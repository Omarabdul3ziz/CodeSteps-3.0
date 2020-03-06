n = input("Enter a number: ")

def fact(num):
    factorial = 1
    if int(num) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
    return factorial

print(fact(n))