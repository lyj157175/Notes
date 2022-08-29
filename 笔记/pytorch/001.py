import torch
import time

'''cuda在大矩阵下计算要比cpu快很多，当小矩阵计算时两者差距不大
    cudnn时用来加速cuda计算的'''

a = torch.randn(1000, 2000)
b = torch.randn(2000, 30000)


t1 = time.time()
y = torch.matmul(a, b)
t2 = time.time()
print(y, t2-t1)


a = torch.randn(1000, 2000).cuda()
b = torch.randn(2000, 3000).cuda()

t1 = time.time()
y = torch.matmul(a, b)
t2 = time.time()
print(y, t2-t1)


