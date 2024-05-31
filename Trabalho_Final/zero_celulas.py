# Importando e carregando as bibliotecas e módulos necessários para rodar esse script
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Função para distribuir zeros aleatórios na tabela de OTUs
def zerar_celulas(tabela, min_zeros=0.45, max_zeros=0.75):
    num_indices = tabela.shape[0]
    for col in tabela.columns:
        num_zeros = np.random.randint(int(min_zeros * num_indices), int(max_zeros * num_indices) + 1)
        zero_indices = np.random.choice(tabela.index, num_zeros, replace=False)
        tabela.loc[zero_indices, col] = 0
    