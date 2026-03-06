while True:
     quantidade_alunos = int(input("Digite o número de alunos que serão cadastrados: "))

     if quantidade_alunos < 10:
          print("O número mínimo de alunos é 10.")
          print("Reinicie o programa e comece do zero.")
          break
        
     for i in range(10):
         
        if quantidade_alunos >= 10:
            nome = input("Digite o nome do aluno: ")

        notas = []

        for i in range(3):
            nota = float(input("Digite uma nota: "))

            if nota < 0 or nota > 10:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
                continue

            notas.append(nota)

        print("Nome:", nome)
        print("Notas:", notas)
        break
     
        