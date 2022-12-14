import pandas as pd
df = pd.read_excel('ex01/arquivo.xlsx',  engine='openpyxl')

df2 = df[df['language'] == 'Python'] #Data Frame somente com as linguagens Python filtradas na coluna "language"
df2.to_csv('ex01/csv1.csv', index=False) #Salvando o Arquivo

df3 = df2.sort_values(by = 'stars', ascending=False).head(50) #Data Frame com os 50 maiores stars de python
df3.to_csv('ex01/csv2.csv', index=False) #Salvando o Arquivo

df4 = df2.sort_values(by = 'forks', ascending=False).head(50) #Data Frame com os 50 maiores forks de python
df4.to_csv('ex01/csv3.csv', index=False) #Salvando o Arquivo