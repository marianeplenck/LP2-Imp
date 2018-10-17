'''#correção AC 5

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
    if taxa > 100 or taxa < 0:
        return -1
    else:
        return valor * taxa / 100
