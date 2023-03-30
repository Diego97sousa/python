#!/usr/bin/env python
# coding: utf-8

# In[69]:


import csv

lista = list()

with open('dados_sensor_01.csv', mode='r', encoding='utf-8') as arq:
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
    for coluna in leitor :  
        if linhas == 0 :
            linhas += 1
        else: 
            print(f'\t{coluna[0]}')
            lista.append(int(coluna[0]))

            linhas += 1 

    arq.close()
            
    temp = len(lista)
  
    
    soma = sum(lista)
   
    
    media = soma/temp
    print('A média das temperaturas é: ', round(media))
            
    media = soma/(len(lista))
    print('A média das temperaturas: ', round(media,2), '°C')

    if soma % 2 == 1:
        mediana = soma/2
    else:
        mediana = (soma /2 + soma /2) /2
    print('A mediana da lista de temperaturas é: ', (mediana),'°C')
    
    calcula = sum(lista) / len(lista)
    varia = sum(lista - mean) **2
    for i in lista / len(lista):
        desvio = varia ** 0.5
        print("A variancia da lista é: ", round(varia,2))
    
   
            


# In[59]:


print(lista)


# In[27]:


temp = len(lista)
print(temp)


# In[17]:


soma = sum(lista)
print(soma)


# In[18]:


media = soma/temp
print(media)


# In[19]:


media = soma/(len(lista))
print('A média das temperaturas: ', round(media,2), '°C')

if soma % 2 == 1:
    mediana = soma/2
else:
    mediana = (soma/2 +soma/2) /2
print('A mediana da lista de temperaturas é: ', mediana, '°C')


# In[ ]:

calcula = sum(lista) / len(lista)
varia = sum(i - calcula) **2
     for i in lista) / len(lista)
desvio = varia ** 0.5
print("A variância das temperaturas é: " ,round(varia,2))

print('O desvio-padrão das temperaturas é: ' round(desvio,2))

arquivo = open ('Relatório_de_temperaturas.txt', 'w')
arquivo.write("Valores total das temperaturas: 5548 °C\N")
arquivo.write("Médi das temperaturas: 22.64°C\N")
arquivo.write("A mediana da lista de temperaturas é: 14.0°C\N")
arquivo.write("A variância da lista é: 108.34°C\N")
arquivo.write("O desvio-padrão da lista é: 10.41°C\N")

arquivo.close()




