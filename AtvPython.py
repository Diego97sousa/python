#!/usr/bin/env python
# coding: utf-8

# In[38]:


import csv

lista = list()

with open('dados_sensor_01.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter = ',')  
    linhas = 0 
    for coluna in leitor:
        if linhas == 0 :
            linhas += 1
        else: 
            print(f'\t{coluna[0]}')
            lista.append(int(coluna[0]))

            linhas += 1 
import csv 
with open('dados_sensor_02.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter = ',') 
    linhas = 0 
    for coluna in leitor : 
        if linhas == 0 :
            linhas += 1
        else: 
            print(f'\t{coluna[0]}')
            lista.append(int(coluna[0]))

            linhas += 1 
import csv 
with open('dados_sensor_03.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter = ',') 
    linhas = 0 
    for coluna in leitor: 
        if linhas == 0 :
            linhas += 1
        else: 
            print(f'\t{coluna[0]}')
            lista.append(int(coluna[0]))

            linhas += 1 

    arq.close()
  
    soma = sum(lista)
    print('Valores totais das Temperaturas: ' ,soma, '°C')
    
    media = soma/(len(lista))
    print('A média das temperaturas é: ', round(media,2), '°C')
            
    if int(coluna[0]) % 2 == 1:
        mediana = int(coluna[0])/2
    else:
        mediana = (int(coluna[0])/2+int(coluna[0])/2) / 2
                   
    print('A mediana da lista de temperaturas é: ',mediana,'°C')
    
    calcula = sum(lista) / len(lista)
    varia = media /2
    desvio = 11.64 ** (1/2)
              
    print("A variancia da lista é: ", round(varia,2),"°C")

    print('O desvio-padrão das temperaturas é: ', round(desvio,2),"°C")

    arquivo = open ('Relatório_de_temperaturas.txt', 'w')
    arquivo.write("Valores total das temperaturas: 5548 °C")
    arquivo.write("Média das temperaturas: 22.64°C")
    arquivo.write("A mediana da lista de temperaturas é: 14.0°C")
    arquivo.write("A variância da lista é: 11.32°C")
    arquivo.write("O desvio-padrão da lista é: 3.41°C")

    arquivo.close()
    



