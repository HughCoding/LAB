import numpy as np
import pandas as pd

datatype = [('data', 'U20'), ('regiao', 'U10'), ('produto', 'U10'),
            ('quantidade_vendida', 'i4'), ('preco_unitario', 'f4'), ('valor_total', 'f4')]

dataset = np.genfromtxt('vendas.csv', delimiter=',', dtype=datatype, skip_header=1)

# Calcule a média, mediana e desvio padrão do Valor Total das vendas
media_valor_total = np.average(dataset['valor_total'])
mediana_valor_total = np.median(dataset['valor_total'])
desvio_valor_total = np.std(dataset['valor_total'])

# Encontre o produto com a maior quantidade vendida e o produto com o maior valor total de vendas.
index_max_quantidade = np.argmax(dataset['quantidade_vendida'])
produto_max_quantidade = dataset['produto'][index_max_quantidade]
quantidade_max = dataset['quantidade_vendida'][index_max_quantidade]

index_max_valor_total = np.argmax(dataset['valor_total'])
produto_max_valor_total = dataset['produto'][index_max_valor_total]
valor_total_max = dataset['valor_total'][index_max_valor_total]

# Calcule o valor total de vendas por região.
regiao_unica = np.unique(dataset['regiao'])
valor_total_regiao = np.zeros(len(regiao_unica))
np.add.at(valor_total_regiao, np.searchsorted(regiao_unica, dataset['regiao']), dataset['valor_total'])

# Determine a venda média por dia.
data_unica = np.unique(dataset['data'])
media_venda_dia = np.zeros(len(data_unica))

for i, data in enumerate(data_unica):
    media_venda_dia[i] = np.sum(dataset['valor_total'][dataset[data] == data])

media_venda_por_dia = np.mean(media_venda_dia)

# Determine o dia da semana com maior número de vendas.
datas = np.array([np.datetime64(data) for data in dataset['data']])
dias_da_semana = (datas.astype('datetime64[D]').view('int') % 7)
vendas_por_dia = np.zeros(7)

for i, dia in enumerate(dias_da_semana):
    vendas_por_dia[dia] += dataset['valor_total'][i]

dia_com_maior_venda = np.argmax(vendas_por_dia)

nome_dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
