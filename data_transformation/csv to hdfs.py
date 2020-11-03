import pandas as pd
from hdfs import InsecureClient
import os

path = "folder path"

client_hdfs = InsecureClient('http://127.0.0.1:50070')

file = os.listdir(path)

for i in range(len(file)):
    df = pd.read_csv(str(file[i]))
    with client_hdfs.write('/user/root/filename.csv', encoding = 'utf-8', permission=777, overwrite=True) as writer:
        df.to_csv(writer)
    print("export "+str(file[i])+"...")

