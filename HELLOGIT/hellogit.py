#CALCULADORA IMC
peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en metros: "))
imc = peso / altura**2
print(f"tu indice de masa corporal es: {imc:.2f}")
if imc < 18.5:
    print("delgadez")
elif imc >= 18.5 and imc < 24.9:
    print("saludable")
elif imc >= 24.9 and imc < 29.9:
    print("sobrepeso")
else:
    print("obesidad")