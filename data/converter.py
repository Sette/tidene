import pandas as pd
import numpy as np

tsv_file='train.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('train.csv',index=False)
