from mineracao import *

while True:
    op = int(input("1) Treinar máquina\n2)Avaliar frase\n3)Sair\nop: "))
    if op == 1:
        treinar()
        testar()
    elif op == 2:
        try:
            classe = recuperaClassificador()
        except:
            treinar()
        finally:
            classe = recuperaClassificador()
        frase = str(input("Digite uma frase: "))
        avaliaFrase(frase, classe)
    elif op == 3:
        break