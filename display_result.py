import matplotlib.pyplot as plt
import numpy

def paint(data):
    y_test, y_predict, ridge_y_pre, lasso_y_pre = data
    plt.figure(figsize=(10, 5))  # 画布大小
    plt.plot(y_test, label='True')
    plt.plot(y_predict, label='Line')
    plt.plot(ridge_y_pre, label='Ridge')
    plt.plot(lasso_y_pre, label='Lasso')
    plt.legend()
    plt.show()
