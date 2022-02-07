import os #Importando a biblioteca OS

print("#"* 60)
#Criar uma variável para receber o IP ou Host a ser "Pingado"
ip_ou_host = input("Digite o IP ou Host a ser verificado: ")

print("-" * 60)

#Chamando a biblioteca OS
os.system('ping -n 6 {}'.format(ip_ou_host))

print("#"* 60)
