#Sequência de Fibonacci
# 1 1 2 3 5 8 13 21 34 55...
'''Crie uma função que recebacomo parâmetro um número natural n(n>0)
e devolva o n-ésimo termo da sequência de fibonacci.'''

'''lógica em def fib6
fib(7) = 8 +5
fib(7) = fib(6) +fib(5)

'''

def fib(n): #versão 1
    a = 1
    b = 1
    c = 1
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c 
    return c 

def fib2(n):#versão 2
    a = 1
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return a

def fib3(n):#versão 3 <atribuição multipla>
    a, b = 1, 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return a

def fib4(n):#versão 4 
    a, b = 1, 1
    for i in range(2, n+1):
        c=a+b
        a, b = b, c
    return a

def fib5(n):#versão 5 
    a, b = 1, 1
    for i in range(2, n+1):
        c= a + b
        a, b = b, c
    return a

def fib6(n):#versão 6
    if n<= 2:
        return 1
    else:
        return fib6(n-1) + fib6(n-2)

#ou

def fib7(n):
    return 1 if n<= 2 else fib7(n-1) + fib7(n-2)


