import IPython.display
from IPython.display import clear_output as clear
import time
import requests

#Coleta de variáveis
total=int(input("Quantos CEPS você gostaria de buscar? \n"))
clear()

for i in range(total):
  cep=input(f"Qual o {i+1}° CEP que você gostaria de buscar? \n")
  #Chama API 
  url = f'https://viacep.com.br/ws/{cep.strip()}/json/'
  response = requests.get(url)
  if response.status_code == 200:
    print('----------------------------------------------------')
    print(f'As informações do {i+1}° cep são: ')
    print('Rua: ' + str({response.json()['logradouro']}))
    print('Bairro: ' + str({response.json()['bairro']}))
    print('Município: ' + str({response.json()['localidade']}))
    print('Estado: ' + str({response.json()['uf']}))
    print('Complemento: ' + str({response.json()['complemento']}))
    print('DDD: ' + str({response.json()['ddd']}))
    print('----------------------------------------------------')
    time.sleep(2)
  else:
    print("CEP digitado inválido")
    time.sleep(3)
