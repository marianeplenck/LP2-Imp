
'''
def funcao_a(a, b):
    c=a  + b
    return c

def funcao_b (x, y):
    z=funcao_a (x, y) + 10
    return z
 '''
#cod com baixo acoplamento 
#mexe em uma função e a outra continua funcionando
'''
def funcao_a(a, b):
    return a  + b

def funcao_b (x, y):
    return funcao_a (x, y) + 10


e =int(input('valor: '))
f =int(input('valor: '))
print(funcao_b(e,f))

'''

'''
exemplo

[1,5[
lista=[1,2,3,4,5]
for i in range # range é uma lista [1,2,3,4,5] 
for i in <lista, tuplas, string, dicionario>:
    print(i)

'''

#exemplos de subtipos e supertipos, herança, encapsulamento
#nome, email, celular, sigla, disciplinas, mensalidade, ra
#n    ,e       ,c      ,s    ,d         ,m             ,r

class Pessoa:
    def __init__(self , n, e, c):
        self.nome = n
        self.email = e
        self.celular = c
      

    def get_nome(self):
        #return self.nome
        return 'Caro(a) %s' % self.nome    
    def get_email(self):
        return self.email
    def get_celular(self):
        return self.celular

    def set_nome(self,nome):
        self.nome = nome
    def set_email(self,email):
        self.email = email
    def set_celular(self, celular):
        self.celular = celular


class Aluno(Pessoa):
    def __init__(self , n, e, c, s, m, r, d=[]):
        super().__init__(n, e, c)
      
        self.sigla = s
        self.disciplinas = d
        self.mensalidade = m
        self.ra=r

    #criar método
    def __repr__(self):
        return 'Aluno: %s | Curso: %s' % (self.nome, self.sigla)

    #getando os atributos(DEVOLVENDO OS VALORES DELES)        
    def get_sigla(self):
        return self.sigla
    def get_disciplinas(self):
        return self.disciplinas        
        #return '%c.%c.%c.' % (self.sigla[0],self.sigla[1], self.sigla[2])
    def get_mensalidade(self):
        return self.mensalidade
        #quero uma string com duas casas de número real
        #return 'R$ %.2f' % self.mensalidade
    def get_ra(self):
        return self.ra



    #setando os atributos (dando valor a eles)   
    def set_sigla(self,sigla):
        self.sigla = sigla
    def set_disiciplinas(self, nova):
        self.disciplinas.append(nova)         
    def set_mensalidade(self, mensalidade):
        self.mensalidade = mensalidade
    def set_ra(self, ra):
        self.ra

#a = Aluno ('zé',z@', 8, 'ADS', 12, 181,'lógica') PARA CHAMAR CLASSE ALUNO
#a.disciplinas PARA CHAMAR A LISTA DISCIPLINAS
#a.get_disciplinas()

class Professor(Pessoa):
    def __init__(self, n, e, c, v):
        super.__init__(n, e, c)
        #self.disciplinas = d
        self.valor_hora= float(v) 
        
          
    #criar método
    def __repr__(self):
        return 'Prof.  %s ' % self.nome

    #getando os atributos(DEVOLVENDO OS VALORES DELES)
    def get_nome(self, n):
        return 'mestre %s' % self.nome     
    def get_valor_hora(self):
        return self.valor_hora

    #setando os atributos (dando valor a eles)
    def set_valor_hora(self, valor):
        self.valor_hora= float(valor)


    











































