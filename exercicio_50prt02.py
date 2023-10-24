velocidade = 60

local_carro = 90

RADAR_1 = 60

LOCAL_1 = 100

RADAR_RANGE = 1  #local onde o local pega o radar

vel_carr = velocidade - RADAR_1

carr_pass = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE)

carr_mult = carr_pass and vel_carr

if vel_carr:
    print("carro passou do limite")

if  carr_pass:
      
    print('carro passou em  radar 1') 

if carr_mult:
    print('carro multado em 1')