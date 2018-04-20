import numpy as np
import pandas as pd

from regression import LinearRegression

data = pd.read_csv('house.csv')

max = data['size'].max()

data['size'] = data['size'].apply(lambda x: x / max)

bedroomMax = data['bedroom'].max()

data['bedroom'] = data['bedroom'].apply(lambda x: x / bedroomMax)

size = data['size'].values

bedroom = data['bedroom'].values

price = data['price'].values

X = np.array([np.ones(len(size)), size, bedroom]).T

Y = np.array(price)

regression = LinearRegression(alpha=0.006, iteration=1000, feature_count=2)

regression.fit(X, Y)

regression.plot()

while (True):
    size = int(input("Enter size of house:"))
    bedroom = int(input("Enter number of bedroom:"))
    print("price:", int(regression.predict(np.array([1, size, bedroom]))))
