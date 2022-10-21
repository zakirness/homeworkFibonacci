#homework 22.10.2022 Zakirov 20KIS-2

n = int(input())

def FibonacciMath(n):
    if n < 0:
        print("exception!!!!")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return FibonacciMath(n - 1) + FibonacciMath(n - 2)

print(FibonacciMath(n))

