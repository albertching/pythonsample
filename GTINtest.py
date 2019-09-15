import pandas as pd
from gtin import GTIN
import time

df = pd.read_csv('products.csv')

df = df.rename(columns = {
   'product_id':'id',
   'european_article_number':'GTIN'
   })

start = time.time()
gtinlist = []
for index, row in df.iterrows():
   if row['GTIN'] == '':
      gtinlist.append(str(GTIN(raw ='0', length=13)))
   else:
      gtinlist.append(str(GTIN(raw =(row['GTIN']), length=13)))
df['GTIN'] = gtinlist
end = time.time()
print(end - start)

df.to_csv('test.csv', index=False)
