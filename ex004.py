'''Faça um progrsms que leia algo pelo teclado 
e mstre na tela o seu tipo primitivo e todas as informações
posiveis sobre ele:'''
a = input("Digite algo:")
print("o tipo primitivo desse valor é {}".format(type(a)))
print("contem so espaços", a.isspace())
print("É numerico", a.isnumeric())
print("Esta em MAUSCULAS", a.isupper())
print("Está em minuculas", a.islower())
print("Tem letras e numeros", a.isalnum())
print("tem so letras", a.isalpha())

