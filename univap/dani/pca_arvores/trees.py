import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


series_comtend_df = pd.read_table('SeriesPFComTend.dat')
mean_radius_table = series_comtend_df.mean()
series_semtend_df = series_comtend_df - mean_radius_table
series_semtend_df.iloc[:,0] = series_comtend_df.iloc[:,0]

# Matriz da série sem tendência
dados = series_semtend_df.iloc[:, 1:].values

matriz_cov = np.cov(dados)

# Substitui ocorrencias de NaN em matriz_cov por 0,
# para poder calcular autovalores e autovetores
matriz_cov[np.isnan(matriz_cov)] = 0

v, w = np.linalg.eig(matriz_cov)

ordem = v.argsort()

maiorautovetor = w[:, ordem[-1]]
segundomaiorautovetor = w[:, ordem[-2]]

Wpca = np.array([maiorautovetor, segundomaiorautovetor])
novos_dados = np.dot(Wpca, dados)

plt.figure(1)
plt.scatter(novos_dados[0, :], novos_dados[1, :])
plt.show()

series_comtend_df.to_csv('SeriesPFComTend.csv')
mean_radius_table.to_csv('mean.csv')
series_semtend_df.to_csv('SeriesPFSemTend.csv')
