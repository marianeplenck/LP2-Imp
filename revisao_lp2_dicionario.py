'''Crie uma função que receba como parâmetro uma string e devolva um dicionário em que as chaves são os caracteres
e os valores de cada chave são o número de ocorrências de caractere na string.'''

#Exemplo caracteres('Banana') -> {'B':1, 'a':3, 'n':2}

'''def caracteres(s): primeira versão
    d={}
    #for i in range(2121213)
    #for item in alguma coisa
    for c in s:
        d[c] = 1 #quase funciona
'''


'''<problema> <se a chave não existe o programa cria e coloca 1, se a    
chave existe o programa não aumenta e sim cria um novo também;>'''

#caracteres('Banana')   <Para chamar no Shell função>

def caractere(s):#lógica para str
    d={}
    for c in s:
        if c in d:

            d[c]=d[c] + 1

        else: 
            d[c]=1

    return d

def test_caractere_1(): #teste que dará certo
    assert caractere('ana') == {'a':2, 'n':1}
    return True #se quiser ver a resposta,se retornar TRUE deu certo caso contrário dá um erro

def test_caractere_2(): #teste que dará errado
    assert caractere('ana') == {'a':777, 'n':1}
    return True #se quiser ver a resposta,se retornar TRUE deu certo caso contrário dá um erro

# desenvolva a lógica para percorrer um int ( com while) 
# estude percorrer um dic. append, etc 
# vai cair uma questão semelhante a esta na prova 

def caracteres(n):#outra versão
    for c in n:
        try:
            d[c]= d[c] + 1
        except KeyError:
            d[c] = 1
    return d


#-------------------------------------------------------------------------------------------------------------------------------
def mostra(lista, i, f):
    #qual o erro que pode acontecer se i>=f
    for i in  range (i, f+1):
        print(lista[j]) # existe problema lógico pq se o inicio começa depois do final não existe lista
        '''-->IndexError'''

