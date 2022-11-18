from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso


def process(x, y):
    if x.shape[0] != y.shape[0]:
        x = x.transpose()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=420)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    estimator = LinearRegression()
    estimator.fit(x_train, y_train)

    print('---------使用线性回归模型预测---------')
    print('权重系数：\n', estimator.coef_)
    print('偏置为：\n', estimator.intercept_)
    y_predict = estimator.predict(x_test)
    print('预测房价：\n', y_predict)
    mse = mean_squared_error(y_test, y_predict)
    print('正规方程-均方误差为：\n', mse)
    line_score = r2_score(y_test, y_predict)
    print('正规方程-决定系数为：\n', line_score)

    print('---------使用岭回归模型预测---------')
    ridge = Ridge()
    ridge.fit(x_train, y_train)
    ridge_y_pre = ridge.predict(x_test)
    ridge_score = r2_score(y_test, ridge_y_pre)
    print('岭回归-决定系数为：\n', ridge_score)

    print('---------使用套索回归模型预测---------')
    lasso = Lasso()
    lasso.fit(x_train, y_train)
    lasso_y_pre = lasso.predict(x_test)
    lasso_score = r2_score(y_test, lasso_y_pre)
    print('套索回归-决定系数为：\n', lasso_score)

    return y_test, y_predict, ridge_y_pre, lasso_y_pre
