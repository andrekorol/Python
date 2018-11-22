import pandas as pd


series_df = pd.read_table('SeriesPFComTend.dat')
print(series_df.mean())