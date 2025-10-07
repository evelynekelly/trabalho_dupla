class SistemaControle:
    def __init__(self):
        self.professores = []
        self.alunos = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno) 

    def remover_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
        else:
            print("Professor não encontrado.")

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
        else:
            print("Aluno não encontrado.")

    def listar_professores(self):
        return self.professores

    def listar_alunos(self):
        return self.alunos