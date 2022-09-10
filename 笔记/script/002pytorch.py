# import torch
# import time
#
# '''cuda在大矩阵下计算要比cpu快很多，当小矩阵计算时两者差距不大
#     cudnn时用来加速cuda计算的'''
#
# a = torch.randn(1000, 2000)
# b = torch.randn(2000, 30000)
#
#
# t1 = time.time()
# y = torch.matmul(a, b)
# t2 = time.time()
# print(y, t2-t1)
#
#
# a = torch.randn(1000, 2000).cuda()
# b = torch.randn(2000, 3000).cuda()
#
# t1 = time.time()
# y = torch.matmul(a, b)
# t2 = time.time()
# print(y, t2-t1)
#
#
# #######################################
# import torch
#
# # 需要模拟的函数
# # y = 3 * x + 5
# x = torch.linspace(0, 10, 10)
# y = 3 * x + 5
# # print(x, y)
#
# # loss = (wx + b - y)^2
# # loss_w = 2(wx + b - y) * x
# # loss_b = 2(wx + b -y)
# w = 0
# b = 0
# lr = 0.01
# for i in range(200):
#     for j in range(len(x)):
#         xi = x[j]
#         yi = y[j]
#         w = w - lr * 2 * (w * xi + b - yi) * xi
#         b = b - lr * 2 * (w * xi + b - yi)
#
#
# # 训练完的w，b
# print(w, b)
#
#
# ################################################
# # 数据格式
# # int -       IntTensor()
# # float -     FloatTensor()
# # int arr -   IntTensor([])
# # float arr - FloatTensor([])
# # string -    embedding()编码的方式
# #
# # a.type()  # 类型推断
# # isinstance(a, torch.FloatTensor)
# #
# # a.shape
# # a.size()
# # a.shape[1]
# # a.size(1)
#
# # a.numel()  # 统计数的个数
#
#
# import torch
# a = torch.tensor(2)  # 生成2的标量
# b = torch.IntTensor(2)  # 生成维度为2的数据
# print(a, b)
#
#
# x = torch.randn(10, 320, 10)
# print(x.numel())
#
# x = torch.empty(2, 3)
# print(x)
#
# y = torch.rand_like(x)
# y = torch.ones_like(x)
# print(y)
#
#
# x = torch.randint(1, 10, (2, 3))
# print(x)
#
# x = torch.full((2, 3), 100)
# print(x)
#
# x = torch.arange(1, 10)
# print(x)
#
#
# a = torch.eye(3, 3)
# b = torch.ones(3, 3)
# c = torch.zeros(3, 3)
#
#
#
#
# import torch
#
# a = torch.tensor([[1,2],[3,4]])
# b = torch.tensor([[1,1],[1,1]])
#
# print(a * b)    # 矩阵相乘
# print(a.matmul(b))   # 矩阵点积 dot-product
#
#



# y = x.detach()
# with torch.no_grad():
#     y = x


## autograd 的使用
def check_autograd():
    import torch
    x=torch.tensor([[1.,2.,3.],[4.,5.,6.]], requires_grad=True)
    # x.requires_grad = True    # x=Variable(x,requires_grad=True)

    y = x + 2
    z = y * y * 3
    out = z.mean()
    out.backward()   # d(out)/d(x) = x + 2


    #查看操作函数
    print(x.grad_fn) # None
    print(y.grad_fn)
    print(z.grad_fn)
    print(out.grad_fn)


    # 反向梯度求导只对自定义的叶子节点，所以是求out对x的偏导数
    print(x.grad)
    print(y.grad)    # None
    print(z.grad)    # None
    print(out.grad)  # None


    # 停止计算梯度
    # with torch.no_grad:
    #     pass
    # copy_ = out.detach()



if __name__ == '__main__':
    check_autograd()
