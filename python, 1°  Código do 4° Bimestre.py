#=====================================
#DESAFIO DEV: MINI-QUIZ DE TECNOLOGIA
#------CABEÇALHO----------
#Aluno: Vinícius Cauã Ribeiro da Silva
#Data: 06/10/2026
#Professor: Rodrigo Vilela
#Turma: 1°A
#Curso: Desenvolvimento de Sistemas
#=====================================

print("=== BEM-VINDO AO QUIZ TECH CEJO/SENAI ===")
nome = input("Digite seu nome: ")
print(f"\nOlá, {nome}! Responda às perguntas com A, B ou C:\n")

pontuacao=0

#--- PERGUNTA 1 ---
print("1) Qual linguagem estamos aprendendo nesta aula?")
print("A) HTML")
print("B) PYTHON")
print("C) C++")
resposta1=input("Sua resposta: ").upper()

if resposta1=="B":
    print("✅Resposta correta! +1 ponto.\n")
    pontuacao=pontuacao+1
else:
    print("❌Resposta incorreta. A certa era B (Python)\n")

#---PERGUNTA 2---
print("2) O que significa a sigla SGBD em Banco de Dados?")
print("A) Sistema de Gerenciamento de Banco de Dados")
print("B) Sistema Geral de Busca Digital")
print("C) Software de Gravação de Baixo Desempenho")
resposta2=input("Sua resposta: ").upper()

if resposta2=="A":
    print("✅Resposta correta! +1 ponto.\n")
    pontuacao=pontuacao+1
else:
    print("❌Resposta incorreta. A certa era A (Sistema de Gerenciamento de Banco de Dados)\n")

#---PERGUNTA 3---
print("3) Qual comando em Python é usado para exibir mensagens na tela?")
print("A) Input()")
print("B) print()")
print("C) Import()")
resposta3=input("Sua resposta: ").upper()

if resposta3=="B":
    print("✅Resposta correta! +1 ponto.\n")
    pontuacao=pontuacao+1
else:
    print("❌Resposta incorreta. A certa era B (print())\n")

#---PERGUNTA 4---
print("4) Para que serve a função print() no Python?")
print("A) Criar uma variável")
print("B) Exibir informações na tela")
print("C) Apagar informações do computador")
resposta4=input("Sua resposta: ").upper()

if resposta4=="B":
    print("✅Resposta correta! +1 ponto.\n")
    pontuacao=pontuacao+1
else:
    print("❌Resposta incorreta. A certa era B (Exibir informações na tela)\n")

#---PERGUNTA 5---
print("5) Para que serve o else em Python?")
print("A) Para repetir um comando")
print("B) Para executar uma ação quando a condição do if não é verdadeira")
print("C) Para criar uma variável")
resposta5=input("Sua resposta: ").upper()

if resposta5=="B":
    print("✅Resposta correta! +1 ponto.\n")
    pontuacao=pontuacao+1
else:
    print("❌Resposta incorreta. A certa era B (Para executar uma ação quando a condição do if não é verdadeira)\n")



#---RESULTADO FINAL ---
print("=================================================")
print(f"Fim do Quiz, {nome}!")
print(f"Sua pontuação final foi: {pontuacao} de 5 pontos.")

if pontuacao == 5:
    print(" Excelente! Você acertou tudo!")
elif pontuacao >= 3:
    print(" Bom trabalho! Dá para melhorar revisando o conteúdo.")
else:
    print(" Precisa estudar mais um pouquinho")
print("===================================================")
