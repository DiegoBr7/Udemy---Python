letra = input('Qual e a palavra ?')

palavra = len(letra)

if palavra < 4:
    print('sua palavra e muito curta')

elif 4 <= palavra <= 6 :
    print('seu nome e normal')   

elif palavra > 6 :
    print('seu nome e muito grande')     