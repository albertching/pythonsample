import logging
import pandas as pd
import numpy as np
from gtin import GTIN
import time

import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

# using logging for output logfile and log on stream 
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('testlog.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)





df = pd.read_csv('products.csv')

#change the column names to fit google file 
df = df.rename(columns = {
   'product_id':'id',
   'product_name':'title',
   'description':'description',
   'deeplink':'link',
   'image_url':'image_link',
   'in_stock':'availability',
   'brand':'brand',
   'european_article_number':'GTIN'
   })

#read columns 
#for col in df.columns:
   #print(col)

#find Nan value
Nan_value = df.isna().values


#NaN column
Nan_col = df.columns[df.isna().any()]

#count NaN per column
num_Nan = df[Nan_col].isna().sum()

for i in range (len(Nan_col)):
   logger.warning('column: {} , NaN per column: {}'
                  .format(Nan_col[i],num_Nan[i]))

#check-digit GTIN
start = time.time()
for i in df.GTIN:
   if i == '':
      i = '0'
   df.loc[df.GTIN == i,['GTIN']]= str(GTIN(raw = i ,length=13))
end = time.time()
print(end - start)
#check 2114770970000 to 21147709700008
#print(df[df.id == 1477097].GTIN)


#check if description is Nan
Nan_value_descr = df.description.isna()


#print(df['price'])

#add currency to price
df.currency = 'GBP'
df.price= df.price.astype(str) + ' ' + df.currency 

#create new csv
df.to_csv('test.csv', index=False)


#kmeans
df = pd.read_csv('products.csv')
df1 = df[['price','product_id']]
pricevalue = df.price.values
productidvalue = df.product_id.values
indexvalue = [i for i in range(len(pricevalue))]

plt.figure(figsize=(10, 7))
plt.title("product Dendograms")
dend = shc.dendrogram(shc.linkage(df1.head().values, method='ward'))




