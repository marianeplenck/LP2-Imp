def menor(lista, i, f):
    try:
        assert i <= f
        m=lista[i]
        for j in range b(i+1, f+1):
            if lista[j]<m:
                m=lista[j]
        return m
    except IndexError as e:
        print('Erro de indice inválido: ', e)
    except Exception as e:
        print ('Erro genérico: ',e)


