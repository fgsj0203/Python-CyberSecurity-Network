#----------------------------------------------------------------------------
#Script utilizado para multiplos hosts
#Detalhe que deve ser criado um arquivo de texto com os hosts nela para que a lista seja percorrida

import os #Importando a biblioteca das funcionalidades da SO
import time #trabalhar com funcionalidades relacionados a tempo

#Acessar o arquivo de texto
with open("hosts") as file:
    dump = file.read() #ler o arquivo
    dump = dump.splitlines() #método usado para remover as linhas em branco, já que o no for abaixo, os dados serão exibidos na vertical

    for ip in dump:
        print("Verificando o IP: ", ip)
        print("-" * 60)
        os.system('ping -n 2 {} '.format(ip))
        print("-" * 60)
        time.sleep(5) #notação em segundos