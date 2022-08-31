import torch
import torch.nn as nn
import math

class BertSelfAttention(nn.Module):
    '''简单实现self-attention = softmax(q * k.t() / sqrt(dk)) * v'''

    def __init__(self):
        super(BertSelfAttention, self).__init__()
        self.dim = 512
        self.q = nn.Linear(self.dim, self.dim)
        self.k = nn.Linear(self.dim, self.dim)
        self.v = nn.Linear(self.dim, self.dim)

        self.softmax = nn.Softmax(-1)

    def forward(self, x):  # x: max_len, dim
        Q = self.q(x)      # max_len, dim
        K = self.k(x)      # max_len, dim
        V = self.v(x)      # max_len, dim

        attention_score = torch.matmul(Q, K.transpose(-1, -2))   # max_len, max_len
        attention_score = self.softmax(attention_score / math.sqrt(self.dim))  # max_len, max_len

        out = torch.matmul(attention_score, V)   # max_len, dim

        return out


if __name__ == '__main__':
    x = torch.randn(8, 512)
    attn = BertSelfAttention()
    out = attn(x)
    print(out.shape)

