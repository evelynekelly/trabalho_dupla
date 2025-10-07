import os

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade



class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
       
    def apresentar(self):
        return f"Professor/a: {self.nome}\n disciplina: {self.disciplina} \n Idade: {self.idade} anos.\n"

    def atribuir_nota(self, aluno, nota):
       if 0 <= nota <= 10:
        aluno.nota = nota
        print(f"A nota do/da aluno/a {aluno.nome} foi registrada como {nota}.")
       else:
        print("Número inválido. A nota deve ser entre 0 e 10.")

    def registrar_presenca(self, aluno, presenca):
        aluno.presenca = presenca.lower()
        if presenca == "sim":
            print(f"O/A aluno/a {aluno.nome} está presente.")

        elif presenca == "não":
            print(f"O/A aluno/a {aluno.nome} faltou.")

        elif presenca == "justificada":
            print(f"A falta do/da aluno/a {aluno.nome} foi justificada.")
        else:
            print("Resposta inválida.")

    




class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso, nota=None, presenca="não registrada"):
        super().__init__(nome, idade)
        
        self.matricula = matricula
        self.curso = curso
        self.nota = nota
        self.presenca = presenca
        


    
    def apresentar(self):
        return f"Estudante: {self.nome}\n Idade: {self.idade} anos \n Curso: {self.curso}.\n"


def mostrar_boletins(sistema):
      print("\n Boletins dos Alunos:")
      for aluno in sistema.listar_alunos():
        nota = getattr(aluno, "nota", "Não atribuída")
        presenca = getattr(aluno, "presenca", "Não registrada")
        print(f"{aluno.nome} | Nota: {nota} | Presença: {presenca}")

def calcular_media(sistema):
     notas = [aluno.nota for aluno in sistema.listar_alunos() if isinstance(aluno.nota, (int, float))]
     if notas:
        media = sum(notas) / len(notas)
        print(f"\n Média da turma: {media:.2f}")
     else:
        print("\n Nenhuma nota registrada para calcular média.")

def buscar_aluno_por_matricula(sistema, matricula):
     for aluno in sistema.listar_alunos():
        if aluno.matricula == matricula:
            print(f"\n Aluno encontrado: {aluno.apresentar()}")
            return aluno
     print(f"\n Nenhum aluno encontrado com a matrícula {matricula}.")


def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")