import pandas as pd
x = pd.ExcelFile('employee.xlsx')
df = x.parse('Sheet1')
df = df.set_index(['ID1', 'ID2'])
df2 = x.parse('Sheet2')
df2 = df2.set_index(['ID1', 'ID2'])
T = df.join(df2).fillna(0)
G = T.groupby('ID1')
print(G.mean())
