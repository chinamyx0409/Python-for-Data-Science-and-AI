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
