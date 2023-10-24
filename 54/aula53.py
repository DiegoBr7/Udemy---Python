condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faca algo")
else:
    print("Nao faca algo")

if passou_no_if is None:
   
    print("Nao passou no If")
else:
    print("Passou no If")



print(passou_no_if , passou_no_if is None)
print(passou_no_if , passou_no_if is not None)