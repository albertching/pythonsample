import numpy as np
import logging
import pandas as pd
from gtin import GTIN
import matplotlib.pyplot as plt
from sklearn import preprocessing
import time

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
   'european_article_number':'EAN'
   })

df.sort_values(["price"], ascending = False)

#check and change GTIN
df['GTIN'] = df.EAN.apply(lambda x: (str(GTIN(int(x),length = 13))))
# if the GTIN is change, return true
df['GTIN_change'] = (df.GTIN != df.EAN.apply(lambda x: (str(x))))
# create new df to check
a = df[['EAN','GTIN','GTIN_change']]
#-------------------------------------
#plot graph
le = preprocessing.LabelEncoder()
df['brand_encoded'] = le.fit_transform(df.brand.values)
brandlist = sorted(list(dict.fromkeys(df.brand)))

df.plot.scatter (x = 'price',
                 y = 'delivery_cost',
                 c = 'brand_encoded',
                 colormap = 'viridis'
                 )







