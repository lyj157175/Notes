# 数据格式
# int -       IntTensor()
# float -     FloatTensor()
# int arr -   IntTensor([])
# float arr - FloatTensor([])
# string -    embedding()编码的方式
#
# a.type()  # 类型推断
# isinstance(a, torch.FloatTensor)
#
# a.shape
# a.size()
# a.shape[1]
# a.size(1)

# a.numel()  # 统计数的个数


import torch
a = torch.tensor(2)  # 生成2的标量
b = torch.IntTensor(2)  # 生成维度为2的数据
print(a, b)



x = torch.randn(10, 320, 10)
print(x.numel())



x = torch.empty(2, 3)
print(x)

y = torch.rand_like(x)
y = torch.ones_like(x)
print(y)


x = torch.randint(1, 10, (2, 3))
print(x)

x = torch.full((2, 3), 100)
print(x)

x = torch.arange(1, 10)
print(x)


a = torch.eye(3, 3)
b = torch.ones(3, 3)
c = torch.zeros(3, 3)

