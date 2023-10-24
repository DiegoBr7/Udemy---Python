numero = input('qual o numero ')
print(numero)

if numero != int:
    print('Esse numero e diferente de inteiro')


if  numero % 2 == 0:
    print('esse numero é par')

else:
    print('Esse numero e impar')

# ---------------------------CHAT GPT--------------------------------------------------------------------------------

while True:
    entrada = input('Digite um número inteiro: ')

    if entrada.isdigit():
        numero = int(entrada)
        if numero % 2 == 0:
            print('Este número é par')
        else:
            print('Este número é ímpar')
        break  # Saímos do loop enquanto a entrada for válida
    else:
        print('Isso não é um número inteiro válido. Tente novamente.')



        

        """
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
