# %%
import pandas as pd


# %%

data_train = pd.read_csv('data/heston/train.csv')

length1 = len(data_train) // 2

df1 = data_train.iloc[:length1, :]
df2 = data_train.iloc[length1:, :]

df1.to_csv('data/heston/train1.csv', index=False)
df2.to_csv('data/heston/train2.csv', index=False)
