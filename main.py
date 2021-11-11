import numpy as np
import pandas as pd
import csv
Data = pd.read_csv("reviews.tsv", sep="\t")
tsv_file = open("reviews.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")

#for row in read_tsv:
#print(row)

df = pd.DataFrame(np.random.randn(100, 2))

msk = np.random.rand(len(df)) < 0.8

train = df[msk]

test = df[~msk]
