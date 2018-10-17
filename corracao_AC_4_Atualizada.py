class Aluno :
    def __init__(self, nome, matricula, nota_ac=0, nota_p=0, faltas=0):
        self.nome= nome
        self.matricula= matricula
        self.nota_ac= nota_ac
        self.nota_p= nota_p
        self.__media= 0,6* nota_ac + 0.4 * nota_p
        self.__faltas=faltas

    def aprovado (self):
        return self.get_media() >= 6 and self.__faltas <= 4
                    
        

    def abona_faltas(self,n):
        if self.__faltas<n:
          print("Não é possivel abonar este numero de faltas")
        else:
            self.__faltas -= n


    def get_media(self):
        return 0.6*self.nota_ac + 0.4 *self.nota_p
        

    def get_faltas(self):
        return self.__faltas

    def set_nota_ac(self,nova):
        self.nota_ac= nova
        

    def set_nota_p(self, nova):
        self.nota_p=nova
        


     

    
a=Aluno ("mariane", "1818")
a.nome="Mariane"
a.abona_faltas(1)
print('média: ', a.get_media())
print('Faltas: ', a.get_faltas())
print('aprovado: ', a.aprovado())



#a.nota_ac=7
a.set_nota_ac(7)
#a.nota_p = 6
a.set_nota_p(10)

print('média: ', a.get_media())
print('Faltas: ', a.get_faltas())
print('aprovado: ', a.aprovado())
