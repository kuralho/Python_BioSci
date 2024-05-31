# Importando e carregando as bibliotecas e módulos necessários para rodar esse script
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Função para realizar a normalização por TSS na OTU_table
def TSS(tabela):
    soma = tabela.sum(axis=0)
    prop = tabela.div(soma)
    vezes = prop*100000
    inteiros = vezes.astype(int)
    return inteiros