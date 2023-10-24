# -----------------------2222222222222-----------------------------------------------------


# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """




# ---------------------------------CHAT GPT-----------------------------------------------

horario = int(input("QUAL o HORARIO ?"))

if horario >= 0 and horario < 12:
    print("Bom dia")
elif horario >= 12 and horario < 18:
    print("Boa tarde")
elif horario >= 18:
    print("Bora tomar uma!")
else:
    print("Madruginhas")
