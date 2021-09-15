#피보나치수열을 Dynamic Programming 으로 구현하는 방법을 알아보자

# naive fibonacci
def fib_naive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_naive(n-1)+fib_naive(n-2)

print(fib_naive(7))
