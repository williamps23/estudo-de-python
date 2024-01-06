'''programa que caucule o almento de um salario
ele deve solicitar o valor do salario e a porcentagem do almento
e exiba o valor do almento e novo salario'''
sal1 = float(input("salario inicial:"))
aumento = float(input("qual o valor do almento:"))
porc = aumento / 100
sal2 = sal1 + aumento
print("olá seu salario aumentou {}%".format(porc))
print("o seu novo saçario é: R$ {}".format(sal2))