# coursera_DataScience
Refer to below gist for data science courses

https://gist.github.com/chinamyx0409

Additonal reading material to week 4 panda dataframe
import pandas as pd # to create data frame
import numpy as np # to randomize number
https://cmdlinetips.com/2020/04/insert-a-column-at-specific-location-in-pandas-dataframe/

Sorting, rename columns
https://www.datacamp.com/community/tutorials/pandas-sort-values?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-517318241987:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9062530&gclid=CjwKCAiAu8SABhAxEiwAsodSZJ2C9mZuXNA7jYDlYapJg11IisoG1wvfTDPnyHaoYbVEOw6KdNYqqxoCNjwQAvD_BwE
https://www.kite.com/python/answers/how-to-update-a-value-in-each-row-of-a-pandas-dataframe-in-python

import Plotly and iPython for Scientific Graphing
https://www.youtube.com/watch?v=zG8FYPFU9n4


#understanding sets, dataframe, list
https://datatofish.com/convert-pandas-dataframe-to-list/
import pandas as pd

#Dictionary: create a dictionary called products
products = {'Product': ['Tablet','iPhone','Laptop','Monitor'],
            'Price': [250,800,1200,300]
            }

#DataFrame: convert the dictionary to a dataframe and assign the values using the keys to columns 'product' and 'price'
df = pd.DataFrame(products, columns= ['Product', 'Price'])

#LIST: convert the dataframe to a list
products_list = df.values.tolist()
print (products_list)


