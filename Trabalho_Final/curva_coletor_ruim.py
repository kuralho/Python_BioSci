# Importando e carregando as bibliotecas e módulos necessários para rodar esse script
import pandas as pd
import numpy as np
from numpy import random
from matplotlib import pyplot, pyplot as plt
import seaborn as sns

def curva_do_coletor(tabela):
    soma = tabela.sum(axis=0)
    prop = tabela.div(soma, axis=1)
    indices = tabela.index.values

    Reads_acum = []
    riqueza_acumulada = []
    num_amostras_acumulado = []

    for col in tabela.columns:
        for n in range(1000, int(soma[col]) + 1, 1000):
            amostra = np.random.choice(indices, p=prop[col].values, size=n, replace=True)
            riqueza_amostra = len(set(amostra))
            riqueza_acumulada.append(riqueza_amostra)
            num_amostras_acumulado.append(n)

    num_amostras_acumulado, riqueza_acumulada = zip(*sorted(zip(num_amostras_acumulado, riqueza_acumulada)))

    plt.plot(num_amostras_acumulado, riqueza_acumulada)
    plt.xlabel('Número acumulado de reads')
    plt.ylabel('Riqueza acumulada (OTUs)')
    plt.title('Curva do Coletor')
    plt.grid(True)
    plt.savefig('Curva do Coletor')   
    plt.show()




