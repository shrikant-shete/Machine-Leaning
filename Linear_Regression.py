import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model

xs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
ys = [10, 10, 20, 22, 21, 25, 30, 21, 21, 34, 35, 30, 50, 45, 55, 60, 66, 64, 67, 72, 74, 80, 79, 84]

xs_shaped = np.reshape(xs, (-1, 1))
linear = linear_model.LinearRegression()
linear.fit(xs_shaped, ys)
linear.score(xs_shaped, ys)
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
t = [27]
x_test = np.reshape(t, (-1, 1))
predicted = linear.predict(x_test)
print('Predicted value for 27=', predicted[0])
plt.scatter(xs, ys)
reg_line = [(linear.coef_*x) + linear.intercept_ for x in xs]
plt.scatter(xs, ys, color='red', marker='o', linestyle='dashed')
plt.plot(xs,reg_line)
plt.show()


