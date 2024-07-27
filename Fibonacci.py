def fibonacci(n):
    fib_seq = []
    a,b = 0,1
    for _ in range(n):
        fib_seq.append(a)
        a,b = b, a+b
    return fib_seq
n= 10
fib_series = fibonacci(n)
print(f"the first {n} number in series are {fib_series}")