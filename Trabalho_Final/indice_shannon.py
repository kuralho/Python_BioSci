# Importando e carregando as bibliotecas e módulos necessários para rodar esse script
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Função para criar ln 
def ln(x):
    return np.log(x + 1e-10)

#Função de Shannon
def Shannon (tabela):
    soma = tabela.sum(axis=0)
    prop = tabela.div(soma)
    log_prop = ln(prop)
    vezes = prop*log_prop
    shannon_indice = -vezes.sum()
    return shannon_indice