import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df= pd.read_csv(r'Data Analysis Challenge Data Set.csv')
df['normalized-losses']=df['normalized-losses'].replace('?',int(100))
df['normalized-losses']=df['normalized-losses'].astype(int)
df['num-of-doors']=df['num-of-doors'].replace('?','four')
df['engine-type']=df['engine-type'].replace({'dohcv':'dohc','ohcv':'ohc','ohcf':'ohc',})
df['price']=df['price'].replace('?',10000).astype(int)
df['peak-rpm']=df['peak-rpm'].replace('?',5200).astype(int)
df['horsepower']=df['horsepower'].replace('?',86).astype(int)
df['stroke']=df['stroke'].replace('?',3.4).astype(float)
df['bore']=df['bore'].replace('?',3.4).astype(float)

df_comp_avg_price = df[['make','price']].groupby("make", as_index = False).mean().rename(columns={'price':'brand_avg_price'})
df = df.merge(df_comp_avg_price, on = 'make')
df['brand_category'] = df['brand_avg_price'].apply(lambda x : "Budget" if x < 10000
                                                     else ("Mid_Range" if 10000 <= x < 20000
                                                           else "Luxury"))
df['mileage'] = df['city-mpg']*0.55 + df['highway-mpg']*0.45
auto = df[['fuel-type', 'aspiration', 'body-style', 'drive-wheels', 'wheel-base', 'length', 'width', 'curb-weight', 'engine-type',
       'num-of-cylinders', 'engine-size',  'bore', 'horsepower', 'price', 'brand_category', 'mileage']]

cyl_no = pd.get_dummies(auto['num-of-cylinders'], drop_first = True)
auto = pd.concat([auto, cyl_no], axis = 1)
brand_cat = pd.get_dummies(auto['brand_category'], drop_first = True)
auto = pd.concat([auto, brand_cat], axis = 1)
eng_typ = pd.get_dummies(auto['engine-type'], drop_first = True)
auto = pd.concat([auto, eng_typ], axis = 1)
drwh = pd.get_dummies(auto['drive-wheels'], drop_first = True)
auto = pd.concat([auto, drwh], axis = 1)
carb = pd.get_dummies(auto['body-style'], drop_first = True)
auto = pd.concat([auto, carb], axis = 1)
asp = pd.get_dummies(auto['aspiration'], drop_first = True)
auto = pd.concat([auto, asp], axis = 1)
fuelt = pd.get_dummies(auto['fuel-type'], drop_first = True)
auto = pd.concat([auto, fuelt], axis = 1)
auto.drop(['fuel-type', 'aspiration', 'body-style', 'drive-wheels', 'engine-type', 'num-of-cylinders','brand_category'], axis = 1, inplace = True)



from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
y=auto['price']
X=auto.drop('price',1)
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=.3)
scaler=MinMaxScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor().fit(X_train_scaled,y_train)
rf.score(X_test_scaled,y_test)


pickle.dump(rf, open('model.pkl','wb'))