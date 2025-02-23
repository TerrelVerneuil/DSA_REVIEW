# classical fibbonaci sequence
# F(n) = F(n-1) + F(n-2)
# F(0) = 0  
import math


def fibbonaci(n):
    if n <= 1: return n
    else: return fibbonaci(n-1) + fibbonaci(n-2)
    
# lucas numbers
# L(n) = L(n-1) + L(n-2)
# L(0) = 2
# L(1) = 1
def lucas(n):
    if n == 0: return 2
    if n == 1: return 1
    return lucas(n-1) + lucas(n-2)
# negafibbonaci sequence

def negafibbonaci(n):
    if n <= 1: return n
    else: return negafibbonaci(n-2) - negafibbonaci(n-1)
    
# tribonacci sequence

def tribonacci(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1
    else: return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

# pentanacci sequence
def pentanacci(n):
    if n <= 3: return 0
    elif n == 4 or n == 5: return 1
    else: return pentanacci(n-1) + pentanacci(n-2) + pentanacci(n-3) + pentanacci(n-4) + pentanacci(n-5)
    

# pell fibonacci numbers
def pell_fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return (2 * pell_fib(n-1)) + pell_fib(n-2)

# Golden Ratio Fibonacci Numbers
# φ = lim (Fn / Fn-1) as n approaches infinity
def golden_ratio_fib(n):
    if n == 0: return 0
    if n == 1: return 1
    phi = (1 + math.sqrt(5)) / 2 
    result = (phi**n - (-phi)**(-n)) / math.sqrt(5)
    return round(result)

print(golden_ratio_fib(10))
# padovan sequence
def padovan(n):
    if n <= 2: return 1
    return padovan(n-2) + padovan(n-3)

print(padovan(14))

# perrin sequence
def perrin(n):
    if n == 0: return 3
    if n == 1: return 0
    if n == 2: return 2
    return perrin (n - 2) + perrin(n - 3)
# gibonacci sequence 
# Modulo Fibonacci Sequence
# Prime-Indexed Fibonacci Numbers


