import pandas as pd

df = pd.read_csv(f'ex02/spring-framework/CBO2010.csv')
for i in range(11, 21):
    x = pd.read_csv(f'ex02/spring-framework/CBO20{i}.csv')
    df.merge(x, how='left', on='COL1')

print(df)