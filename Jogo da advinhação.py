#=======================================
#JOGO DA ADIVINHAÇÃO DE NÚMEROS
    #------CABEÇALHO----------
#Aluno: Vinícius Cauã Ribeiro da Silva
#Data: 06/10/2026
#Professor: Rodrigo Vilela
#Turma: 1°A
#Curso: Desenvolvimento de Sistemas
#=======================================


numero_secreto = 8 #Número pode ser alterado

print("=== JOGO DA ADIVINHAÇÃO DO CEJO ===")
jogador =input("Digite seu nome: ")
print(f"\n Olá {jogador}! Tente adivinhar o número secreto entre 1 e 10")

chute =int(input("Qual é o seu palpite? "))

if chute==numero_secreto:
    print(f"\n PARABÉNS, {jogador}! Você acertou! O número secreto era {numero_secreto}.")
elif chute>numero_secreto:
    print(f"\n Que pena! O seu chute ({chute}) foi MAIOR do que o número secreto.")
else:
    print(f"\n Que pena! O seu chute ({chute}) foi MENOR do que o número secreto.")

print("\n Obrigado por jogar!")
