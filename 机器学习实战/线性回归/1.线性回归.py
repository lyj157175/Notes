import numpy as np 
import matplotlib.pyplot as ply



def load_data():
    data = np.loadtxt('data/data1.txt', delimiter=',')
    m = data.shape[1]  # 特征维度
    x = data[:, 0:m]
    y = data[:, -1].reshape(-1, 1)
    return x, y


# 归一化：减均值除方差
def feature_normalize(x):
    mean = np.average(x, axis=0)
    std = np.std(x, axis=0, ddof=1)
    x = (x - mean) / std
    return x


def loss(x, y, hi):
    m = x.shape[0]
    loss = np.sum(np.power(np.dot(x, hi) - y, 2)) / 2*m
    return loss


def gradient_descent(x, y, theta, epochs, alpha):






if __name__ == '__main__':
    x, y = load_data()
    x = feature_normalize(x)
    theta = np.zeros(x.shape[1] + 1).reshape(-1, 1)
    epochs = 100
    alpha = 0.01
    theta, loss = gradient_descent(x, y, epochs, theta, alpha)
    






