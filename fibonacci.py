#The fibonacci series is a series such at each number is the preceding sums of the previous 2 numbers. Starting from 0 and 1. write a program to output the first 100 Fibonacci numbers.

for a in range(100):
    b = 1
    c = 1
    for i in range(3, a+ 1):
        Fib = b
        b = c+ b
        c= Fib
    print(b)
