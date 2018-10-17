class Aluno:
    def __init__(self):
        self.nome="Mariane"
        self.matricula= 1010
        self.media=9.9
        self.faltas=1

    def aprovado (self):
        return self.media >= 6 and self. faltas <= 4

    def abona_faltas(self,n):
      self.faltas-=n

a=Aluno()
a.nome="Matheus"
a.matricula="1212"
print('Aprovado:', a.aprovado())
a.abona_faltas(1)

