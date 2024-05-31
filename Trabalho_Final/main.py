# Importando e carregando as bibliotecas e módulos necessários para rodar esse script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns
from zero_celulas import zerar_celulas
from norm_TSS import TSS
from norm_RAREF import RAREF
from indice_shannon import Shannon
from scipy.spatial.distance import pdist
from scipy.stats import f_oneway
from curva_coletor_ruim import curva_do_coletor



##############Simulando uma tabela de OTUs######################
#A função np.random.seed() foi usada para manter a reprodutibilidade da simulação
np.random.seed(77)

#Tabela de OTU por array
num = list(range(4000))
tabela = np.array([random.choice(num, size=26, replace=True) for _ in list(range(100))])
tabela.sum(axis=0)

#Transformando o array em tabela com os nomes das colunas e linhas
colunas = [chr(i) for i in range(ord('A'), ord('Z')+1)]
indices = [f'OTU_{i}' for i in range(100)]
OTU_table = pd.DataFrame(tabela, columns=colunas, index=indices)

#Chamando a tabela pronta
OTU_table

#Salvando a tabela recém gereda
OTU_table.to_csv('OTU_table.tsv', sep = '\t', header = True)

#Soma das colunas para verificação da quantidade de reads (máximo e 100000)
OTU_table.sum(axis = 0)

#Adicionando zeros aleatórios na tabela
zerar_celulas(OTU_table)

#Verificando a tabela de OTU com os zeros
OTU_table

#Abrindo a tabela de OTU
OTU_table = pd.read_csv('OTU_table.tsv', sep='\t', index_col=0)

#Realizando a normalização da OTU_table pelo TSS e rarefação

#Aplicando a função do TSS
OTU_tableTSS = TSS(OTU_table)

#Salvando a tabela de TSS
OTU_tableTSS.to_csv('OTU_tableTSS.tsv', sep = '\t', header = True)

#Aplicando a função de rarefação
OTU_tableRAREF = RAREF(OTU_table)

#Salvando a tabela de rarefação
OTU_tableRAREF.to_csv('OTU_tableRAREF.tsv', sep = '\t', header = True)

#Abrindo as tabelas de OTU_tableTSS e OTU_tableRAREF
OTU_tableTSS = pd.read_csv('OTU_tableTSS.tsv', sep='\t', index_col=0)
OTU_tableRAREF = pd.read_csv('OTU_tableRAREF.tsv', sep='\t', index_col=0)

#Calculando as médias e os desvios padrões para cada tabela criada
Orig_soma = OTU_table.sum()
TSS_table_soma = OTU_tableTSS.sum()
RAREF_table_soma = OTU_tableRAREF.sum()

Orig_soma = pd.DataFrame(OTU_table.sum(), columns = ['Original'])
TSS_table_soma = pd.DataFrame(OTU_tableTSS.sum(), columns = ['TSS'])
RAREF_table_soma = pd.DataFrame(OTU_tableRAREF.sum(), columns = ['Rarefação'])

## Concatenando a soma - PARA O BOXPLOT
Tabela_soma = pd.concat([Orig_soma, TSS_table_soma, RAREF_table_soma], axis = 1)

#Médias das somas
Orig_media = int(Orig_soma.mean())
TSS_media = int(TSS_table_soma.mean())
RAREF_media = int(RAREF_table_soma.mean())

#Desvios padrões das somas
Orig_dp = int(Orig_soma.std())
TSS_dp = int(TSS_table_soma.std())
RAREF_dp = int(RAREF_table_soma.std())

#Tabela contendo as médias e os desvios
Tabela_MDP = {
    'Média': [Orig_media, TSS_media, RAREF_media], 
    'Desvio Padrão': [Orig_dp, TSS_dp, RAREF_dp]
}

linhas_tabela = ['Original', 'TSS', 'RAREF']
Tabela_MDP = pd.DataFrame(Tabela_MDP, index = linhas_tabela)

#Salvando a tabela de médias e desvios
Tabela_MDP.to_csv('Tabela_MDP.tsv', sep = '\t', header = True)

#Aplicando a função do índice de Shannon para cada tabela
Sh_OTU = Shannon(OTU_table)
Sh_TSS = Shannon(OTU_tableTSS)
Sh_RAREF = Shannon(OTU_tableRAREF)

#Criando uma tabela com os índices de Shannon
Sh_OTU = pd.DataFrame(Sh_OTU, columns = ['Original'])
Sh_TSS = pd.DataFrame(Sh_TSS, columns = ['TSS'])
Sh_RAREF = pd.DataFrame(Sh_RAREF, columns = ['RAREF'])

#Concatenando cada tabela
Shannon_table = pd.concat([Sh_OTU, Sh_TSS, Sh_RAREF], axis = 1)

#Salvando a tabela de Shannon
Shannon_table.to_csv('Shannon_table.tsv', sep = '\t', header = True)

#Verificando se há diferenças significativas entre as tabelas
anova_shannon = f_oneway(
        Sh_OTU['Original'],
        Sh_TSS['TSS'],
        Sh_RAREF['RAREF']
    )

print('Resultado da ANOVA:', anova_shannon)

#Função da curva do coletor - infelizmente não está boa
curva_do_coletor(OTU_table)
curva_do_coletor(OTU_tableTSS)
curva_do_coletor(OTU_tableRAREF)

#Para betadiversidade - dissimilaridade de Bray-Curtis 
def braycurtis(tabela1, tabela2):
        return pdist(np.array([tabela1, tabela2]), metric='braycurtis')[0]
amostras = OTU_table.columns[1:]

bray_orig_vs_TSS = {
        amostra: braycurtis(OTU_table[amostra].values, OTU_tableTSS[amostra].values)
        for amostra in amostras
    }

bray_orig_vs_RAREF = {
        amostra: braycurtis(OTU_table[amostra].values, OTU_tableRAREF[amostra].values)
        for amostra in amostras
    }

Bray_dissimilaridade = pd.DataFrame({
        'Amostra': amostras,
        'Dissimilaridade_RAREF': list(bray_orig_vs_RAREF.values()),
        'Dissimilaridade_TSS': list(bray_orig_vs_TSS.values())
    })


#Gráficos
#Boxplot - Shannon
plt.figure(figsize = (15, 9))
plt.boxplot(Shannon_table, tick_labels = ['Original', 'TSS', 'RAREF'])
plt.title("BoxPlot índice de Shannon")
plt.xlabel("Tabelas")
plt.ylabel("Valores do índice de Shannon")
plt.savefig('BoxPlot SHANNON')
plt.close()

###boxplot - Soma
plt.figure(figsize = (15, 9))
plt.boxplot(Tabela_soma, tick_labels = ['Original', 'TSS', 'RAREF'])
plt.title("BoxPlot da amostragem original e as normalizadas")
plt.xlabel("Tabelas")
plt.ylabel("Soma de reads")
plt.savefig('BoxPlot TABELAS_SOMA')
plt.close()

plt.show()

####Diferença entre as colunas

Diferenca_TSS = OTU_table - (OTU_tableTSS)
#Deixando positivo
Diferenca_TSSN = -Diferenca_TSS

Diferenca_RAREF = OTU_table - OTU_tableRAREF

Dif_sumTSS = Diferenca_TSSN.sum(axis = 0)
Dif_sumRAREF = Diferenca_RAREF.sum(axis = 0)

Dif_sumTSS = pd.DataFrame(Diferenca_TSSN.sum(), columns = ['TSS'])
Dif_sumRAREF = pd.DataFrame(Diferenca_RAREF.sum(), columns = ['RAREF'])


Tabela_diferenca = pd.concat([Dif_sumTSS, Dif_sumRAREF], axis = 1)
###boxplot - Diferença entre as normalizações e a original
plt.figure(figsize = (15, 9))
plt.boxplot(Tabela_diferenca, tick_labels = ['TSS', 'RAREF'])
plt.title("BoxPlot da amostragem original e as normalizadas")
plt.xlabel("Tabelas")
plt.ylabel("Soma de reads")
plt.savefig('BoxPlot TABELAS')
plt.close()

print('Trabalho concluído, com amor')

if __name__ != '__main__':
    main()  
    



