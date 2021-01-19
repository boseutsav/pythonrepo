import pandas as pd

df1 = pd.DataFrame({'h1':[20,30,40,50],'h2':[22,33,44,55],'h3':[23,34,45,67]},index=[0,1,2,3])
print(df1)
print('*'*2*len(df1))
df = df1.rename(columns={'h1':'p1','h2':'p2','h3':'p3'})
print(df.loc[1])