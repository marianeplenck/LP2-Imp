'''Crie uma função que receba como parâmetro uma string e devolva um dicionário em que as chaves são os caracteres
e os valores de cada chave são o número de ocorrências de caractere na string.'''

#Exemplo caracteres('Banana') -> {'B':1, 'a':3, 'n':2}

def caracteres(s):
    d={}
    #for i in range(2121213)
    #for item in alguma coisa
    for c in s:
        d[c] = 1 #quase funciona

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


#desenvolva a lógica para percorrer um int ( com while) 
# estude percorrer um dic. append, etc 
# vai cair uma questão semelhante a esta na prova        

