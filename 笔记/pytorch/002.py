import torch

# 需要模拟的函数
# y = 3 * x + 5
x = torch.linspace(0, 10, 10)
y = 3 * x + 5
# print(x, y)

# loss = (wx + b - y)^2
# loss_w = 2(wx + b - y) * x
# loss_b = 2(wx + b -y)
w = 0
b = 0
lr = 0.01
for i in range(200):
    for j in range(len(x)):
        xi = x[j]
        yi = y[j]
        w = w - lr * 2 * (w * xi + b - yi) * xi
        b = b - lr * 2 * (w * xi + b - yi)


# 训练完的w，b
print(w, b)

