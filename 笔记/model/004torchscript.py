import torch  # This is all you need to use both PyTorch and TorchScript!
import torch.nn as nn

# 为方便pytorch模型部署，推出torchscript来追踪网络结构，有trace和script两种方式，其实onnx就是trace方式导出模型

class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.embed = nn.Embedding(100, 100)
        self.lstm = nn.LSTM(input_size=100, hidden_size=256, batch_first=True, bidirectional=False)
        self.fc = nn.Linear(256, 5)

    def forward(self, x):
        embed = self.embed(x)
        lstm_out = self.lstm(embed)  # 2, 8, 256
        out = self.fc(lstm_out[0])
        return out

    @torch.jit.export
    def fun(self, x):
        x = 10* x
        embed = self.embed(x)
        lstm_out = self.lstm(embed)  # 2, 8, 256
        out = self.fc(lstm_out[0])
        return out, out


if __name__ == "__main__":
    model = MyModel()
    x = torch.tensor([[1,2,3,4], [2,3,4,5,]])

    out = model(x)
    print(out)

    model_jit = torch.jit.script(model)
    out_jit = model_jit(x)
    print(out_jit)

    # 打印信息
    print(model_jit.graph)
    print(model_jit.code)
    # model_jit.save('model_jit.pt')
    # mode_jit_load = torch.jit.load('./model_jit.pt')
    # print(mode_jit_load(x))
