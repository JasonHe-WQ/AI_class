from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def process(x, y):
    if x.shape[0] != y.shape[0]:
        x = x.transpose()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=420)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)
    print('权重系数：\n', estimator.coef_)
    print('偏置为：\n', estimator.intercept_)
    y_predict = estimator.predict(x_test)
    print('预测房价：\n', y_predict)
    mse = mean_squared_error(y_test, y_predict)
    print('正规方程-均方误差为：\n', mse)
    return estimator.coef_, estimator.intercept_, y_predict, mse

