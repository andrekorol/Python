import pandas as pd


series_comtend_df = pd.read_table('SeriesPFComTend.dat')
mean_radius_table = series_comtend_df.mean()
series_semtend_df = series_comtend_df - mean_radius_table
series_semtend_df.iloc[:,0] = series_comtend_df.iloc[:,0]

series_comtend_df.to_csv('SeriesPFComTend.csv')
mean_radius_table.to_csv('mean.csv')
series_semtend_df.to_csv('SeriesPFSemTend.csv')
