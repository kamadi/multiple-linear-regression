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

m = len(size)

x0 = np.ones(m)

X = np.array([x0, size, bedroom]).T

Y = np.array(price)

regression = LinearRegression(alpha=0.000009, iteration=125, feature_count=2)

regression.fit(X, Y)

print(int(regression.predict(np.array([1, 2104, 3]))))
