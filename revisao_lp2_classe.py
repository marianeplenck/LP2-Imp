''' não éobrigatório ter init(porém foi dado em aula e cairá em PROVAAAA!!!!!
ESTUDEEEEE)
'''
class Pessoa:#classe mãe
    def __init__(self,n):
        self.__nome=n



class Aluno:
    def __init__(self, n, r, d=[]):#d é parâmetro default e toda função pode ter parâmetro default
        super().__init__(n)#herança
        self.__nome = n #privado
        self.__ra = r #privado
        self.__mensalidade = 690.00 #privado
        self.__disciplinas = d #privado

    def get_nome(self):
        return self.nome
    def set_nome(self, novo):
        self.nome = novo





    

    

