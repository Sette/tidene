import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

tsv_file='train.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('train_complete.csv',index=False)


tsv_file='train.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
corpus , corpus_test =  train_test_split(csv_table, train_size=0.3)
corpus.to_csv('train_min.csv',index=False)
