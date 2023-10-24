numero_srt = input(
    'Vou dobrar o numero que vc digitar: ' 
)
# if numero_srt.isdigit():
#   

try:
      print('STR:' , numero_srt)
      numero_float = float(numero_srt)
      print('FLOAT' , numero_float)
      print(f'O dobro de {numero_srt} é {numero_float * 2:.2f}')
except:
      print('isso nao e um numero')
