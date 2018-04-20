import numpy as np
import pandas as pd

from regression import LinearRegression

data = pd.read_csv('almaty.csv')

max = data['size'].max()

data['size'] = data['size'].apply(lambda x: x / max)

max = data['room'].max()

data['room'] = data['room'].apply(lambda x: x / max)

max = data['year'].max()

data['year'] = data['year'].apply(lambda x: x / max)

max = data['floor'].max()

data['floor'] = data['floor'].apply(lambda x: x / max)

max = data['top_floor'].max()

data['top_floor'] = data['top_floor'].apply(lambda x: x / max)

price = data['price'].values

X = np.array([np.ones(len(price)), data['size'].values, data['room'].values, data['year'].values, data['floor'].values, data['top_floor'].values]).T

Y = np.array(price)

regression = LinearRegression(alpha=0.000001, iteration=300, feature_count=5)

regression.fit(X, Y)

regression.plot()

print("price:", "13800000")
print("price:", int(regression.predict(np.array([1, 45,2,1977,5,5]))))
print()
print("price:", "15333333")
print("price:", int(regression.predict(np.array([1, 40,2,1967,1,4]))))

# while (True):
#     size = int(input("Enter size of house:"))
#     bedroom = int(input("Enter number of bedroom:"))
#     print("price:", int(regression.predict(np.array([1, size, bedroom]))))

# 14700000
# 4298128


# regression = LinearRegression(alpha=0.0003, iteration=600, feature_count=2)
