class Aluno:
    def __init__(self, n, e, c,  m):
        self.nome = n
        self.email = e
        self.celular = c
        self.sigla = s
        #self.disciplinas = d
        self.mensalidade = m

    #criar método
    def __repr__(self):
        return 'Nome: %s | Curso: %s' % \
            (self.nome, self.sigla)

    def get_nome(self):
        return self.nome
        #return 'Mestre %s' % self.nome
    
    def get_email(self):
        return self.email

    def get_celular(self):
        return self.celular

    def get_sigla(self):
        return self.sigla

    #def get_disciplinas(self):
        #return self.disciplinas        
        #return '%c.%c.%c.' % (self.sigla[0],self.sigla[1], self.sigla[2])

    def get_mensalidade(self):
        return self.mensalidade
        #quero uma string com duas casas de número real
        #return 'R$ %.2f' % self.mensalidade

    def set_nome(self,nome):
        self.nome = nome

    def set_email(self,email):
        self.email = email

    def set_celular(self, celular):
        self.celular = celular

    def set_sigla(self,sigla):
        self.sigla = sigla

    #def set_disiciplinas(self, disciplinas):
        #self.disciplinas = disciplinas
           

    def set_mensalidade(self, mensalidade):
        self.mensalidade = mensalidade
