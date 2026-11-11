#Calculadora de IMC
print ("Está es una calculadora de IMC -- jhair flores")
peso = float (input ("Ingresa tu peso en KG (ejemplo: 43, 56, 70): "))
altura = float(input ("Ingresa tu peso en metros (ejemplo: 1.70, 1.56, 1.80): "))
imc =float( peso /  (altura ** 2))
print (f"Tu  imc es el sigueinte: {imc: .2f}")

