# Importando e carregando as bibliotecas e módulos necessários para rodar esse script
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Função para realizar a rarefação na OTU_table
def RAREF (tabela_OTU):

    soma = tabela_OTU.sum(axis=0)
    valor_min = soma.min()
    prop_table = tabela_OTU/tabela_OTU.sum(axis=0)
    OTU_raref = pd.DataFrame(index = tabela_OTU.index, columns = tabela_OTU.columns)

    for coluna in tabela_OTU.columns:
        prop_OTU = prop_table[coluna]
        coluna_rarefeita = np.zeros(len(prop_OTU)).astype(int)
        ctrl1 = 0

        while ctrl1 < valor_min:
            otu_cell = np.random.choice(prop_OTU.index, p = prop_OTU)
            coluna_rarefeita[prop_OTU.index.get_loc(otu_cell)] += 1
            ctrl1 += 1
        OTU_raref[coluna] = coluna_rarefeita

    return OTU_raref