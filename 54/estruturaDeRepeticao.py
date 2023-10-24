condicao = True


#loop infinito:
# while condicao:
#     print(1)
#     print(2)
#     print(3)
#     print(4)


while condicao:
    nome = input("Qual e seu nome ? ")
    print(f"Seu nome é: {nome}")

    if nome == 'sair':
      break