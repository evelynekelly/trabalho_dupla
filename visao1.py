from modelo import Aluno , Professor , mostrar_boletins, calcular_media , buscar_aluno_por_matricula 
from controle import SistemaControle
from modelo import limpar_terminal

if __name__ == "__main__":
     
     sistema = SistemaControle()

    # Alunos iniciais
     sistema.adicionar_aluno(Aluno("Vitória", 21, "101902", "ADS"))
     sistema.adicionar_aluno(Aluno("Mariana", 18, "061106", "ADS"))
     sistema.adicionar_aluno(Aluno("Carlos", 22, "123456", "ADS"))
     sistema.adicionar_aluno(Aluno("Ana", 20, "654321", "ADS"))

    # Professores iniciais
     sistema.adicionar_professor(Professor("João", 45, "Inglês"))
     sistema.adicionar_professor(Professor("Maria", 38, "Matemática"))

     while True:
        limpar_terminal()
        print("===== MENU PRINCIPAL =====\n")
        print("1. Cadastrar aluno")
        print("2. Cadastrar professor")
        print("3. Atribuir Nota")
        print("4. Registrar Presença")
        print("5. Mostrar Boletins")
        print("6. Calcular Média da Turma")
        print("7. Buscar Aluno por Matrícula")
        print("8.  Listar alunos")
        print("9. Listar professores")
        print("10. Remover Aluno")
        print("11. Remover Professor")
        print("12. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            limpar_terminal()
            print("➕ Adicionar Novo Aluno")
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            matricula = input("Matrícula: ")
            curso = input("Curso: ")
            sistema.adicionar_aluno(Aluno(nome, idade, matricula, curso))
            print(f"\n✅ Aluno {nome} adicionado com sucesso!")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "2":
            limpar_terminal()
            print("➕ Adicionar Novo Professor")
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            disciplina = input("Disciplina: ")
            sistema.adicionar_professor(Professor(nome, idade, disciplina))
            print(f"\n✅ Professor {nome} adicionado com sucesso!")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "3":
            limpar_terminal()
            matricula = input("Digite a matrícula do aluno: ")
            aluno = buscar_aluno_por_matricula(sistema, matricula)
            if aluno:
                try:
                    nota = float(input(f"Digite a nota para {aluno.nome} (0 a 10): "))
                    sistema.professores[0].atribuir_nota(aluno, nota)
                except ValueError:
                    print("⚠️ Nota inválida!")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "4":
            limpar_terminal()
            matricula = input("Digite a matrícula do aluno: ")
            aluno = buscar_aluno_por_matricula(sistema, matricula)
            if aluno:
                presenca = input("Presença (sim / não / justificada): ").strip().lower()
                sistema.professores[0].registrar_presenca(aluno, presenca)
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "5":
            limpar_terminal()
            mostrar_boletins(sistema)
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "6":
            limpar_terminal()
            calcular_media(sistema)
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "7":
            limpar_terminal()
            matricula = input("Digite a matrícula do aluno: ")
            buscar_aluno_por_matricula(sistema, matricula)
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "8": 

            limpar_terminal()
            print("👨‍🎓 Alunos:")
            for aluno in sistema.listar_alunos():
                print(aluno.apresentar())
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "9":

            limpar_terminal()
            print("👩‍🏫 Professores:")
            for prof in sistema.listar_professores():
                print(prof.apresentar())
            input("\nPressione Enter para voltar ao menu...")


        elif opcao == "10":

            limpar_terminal()
            print("🗑️ Remover Aluno")
            matricula = input("Digite a matrícula do aluno a ser removido: ")
            aluno_encontrado = None
            for aluno in sistema.listar_alunos():
                if aluno.matricula == matricula:
                    aluno_encontrado = aluno
                    break
            if aluno_encontrado:
                sistema.alunos.remove(aluno_encontrado)
                print(f"\n✅ Aluno {aluno_encontrado.nome} removido com sucesso.")
            else:
                print("\n❌ Aluno não encontrado.")
            input("\nPressione Enter para voltar ao menu...")

        
        
        elif opcao == "11":
           limpar_terminal()
           print("🗑️ Remover Professor")
           nome = input("Digite o nome do professor a ser removido: ").strip()
           professor_encontrado = None
           for prof in sistema.listar_professores():
                if prof.nome.lower() == nome.lower():
                    professor_encontrado = prof
                    break
           if professor_encontrado:
                sistema.professores.remove(professor_encontrado)
                print(f"\n✅ Professor {professor_encontrado.nome} removido com sucesso.")
           else:
                print("\n❌ Professor não encontrado.")
           input("\nPressione Enter para voltar ao menu...")

 

        elif opcao == "12":
           print("Saindo do sistema!!!")
           break 

        else:
            print("❌ Opção inválida.")
            input("\nPressione Enter para voltar ao menu...")