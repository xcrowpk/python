#saludo = "hola "
#nombre = input("ingrese su nombre: ")
#print (saludo + nombre)

#num1 = int(input("ingresar nro1: "))
#num2 = int(input("ingresar nro2: "))
#num3 = int(input("ingresar nro2: "))
#prom = (num1 + num2 + num3) / 3
#print ("el promedio es %.2f"%prom)
#if (prom >= 6):
#	print("aprovado")
#else:
#	print("desaprobado")

#num = int(input("ingresar nota "))
#prom = 0
#cant = 0
#while(num !=0):
#	if(num >= 0 and num <= 10):
#		prom = num + prom
#		cant = cant + 1
#		num = int(input("ingresar nota "))
#	else:
#		num = int(input("ingresar nota entre 1 y 10 o 0 para salir "))	
#		
#print("prom %.2f y cant %i"% (prom,cant))
#prom_final = prom / cant
#print("promedio final %.2f"%prom_final)

...


import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

#if(dado1 < dado2 and dado1 < dado3 and dado1 < dado4):
#	suma = dado2 + dado3 + dado4
#if(dado2 < dado1 and dado2 < dado3 and dado2 < dado4):
#	suma = dado1 + dado3 + dado4
#if(dado3 < dado1 and dado3 < dado2 and dado3 < dado4):
#	suma = dado1 + dado3 + dado4
#if(dado4 < dado1 and dado4 < dado2 and dado4 < dado3):
#	suma = dado1 + dado2 + dado3

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)
res = suma - menor

print ("Fuerza: %i"% res)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)
res = suma - menor

print ("Destreza: %i"% res)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)
res = suma - menor

print ("Constitucion: %i"% res)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)
res = suma - menor

print ("Inteligencia: %i"% res)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)
res = suma - menor

print ("Carisma: %i"% res)











