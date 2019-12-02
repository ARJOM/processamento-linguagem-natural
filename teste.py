from mineracao import *

while True:
    op = int(input("1) Treinar máquina\n2)Avaliar frase\n3)Sair\nop: "))
    if op == 1:
        treinar()
    elif op == 2:
        classe = recuperaClassificador()
        avaliaFrase("eu tenho medo de amar", classe)
    elif op == 3:
        break