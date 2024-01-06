'''programa que leia a quantidade de dias, horas, minutos e segundos de um usuario
e calcule o total em segundos'''
dias = int(input("digite os dias:"))
horas = int(input("digitr as horas:"))
minutos = int(input("digite os minutos:"))
segundos = int(input("digite os segundos:"))
total = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print("O total de tempo gasto foi de {} segundo(s)".format(total))

