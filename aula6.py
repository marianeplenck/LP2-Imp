'''def triangulo(a,b,c):
    if a ==b==c:return 'equilatero'
    if a!= b and b !=c and a!= c: return 'escaleno'
    return 'isósceles'

def test_tri_1():
    assert triangulo (5,5,5) == 'equilatero'

def test_tri_2():
    assert triangulo (5,6,7) == 'escaleno'

def test_tri_3():
    assert triangulo (5,6,5) == 'isósceles'

def test_tri_4():
    assert triangulo (6,6,5) == 'isósceles'


#correção AC 5

def termial(n):
    t = 0
    for i in range (1, n+1):
        t= t + i
    return t

def test_termial_1(): #correto
    assert termial (5) == 15

def test_termial_2(): #correto
    assert termial (6) == 21

def test_termial_3(): #correto
    assert termial (4) == 10

def test_termial_4(): #incorreto
    assert termial (0) == 1500 

'''

def porcentagem(valor, taxa):
    if (taxa > 100 or taxa < 0):
        return -1
    else:
        return valor * taxa / 100

        




