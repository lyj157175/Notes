import torch
import torch.nn as nn
from transformers import AutoConfig, AutoModel, BertModel, BertTokenizer


# 查看模型结构
def check_model(model):
    # print(model.state_dict())
    # print(list(model.named_parameters()))
    # print(model.embeddings)
    # print(model.embeddings.LayerNorm)
    # print(model.encoder.layer[0])
    # print(model.encoder.layer[0].attention.self.query)

    for name, param in model.named_parameters():
        print(name, param)


def count_model_params(model):
    '''计算模型参数'''
    # sum1 = sum(p.numel() for p in model.parameters())
    # sum2 = sum(p.numel() for p in model.parameters() if p.requires_grad)

    count_param = 0
    for name, param in model.named_parameters():
        if len(param.size()) == 2:
            count_param += param.size(0)*param.size(1)
        else:
            count_param += param.size(0)

    print(count_param)



def forward_bert(model):
    input_ids = torch.tensor([[1,2,3,4,5,6,7,8]]).long()
    attention_mask = torch.tensor([[1,1,1,0,0,0,0,0]])
    token_type_ids = torch.tensor([[0,0,0,0,0,0,0,0]])
    out = model(input_ids, attention_mask, token_type_ids)
    print(out.last_hidden_state.shape)  # b, max_len, hidden_size
    print(out.pooler_output.shape)      # b, hidden_size



def test_layer_norm():
    '''
    y = (x - mean) / (var(x) + eps) * alpha + beta
    '''
    # 使用nn.LayerNorm
    batch_size, max_len, dim = 2, 10, 512
    x = torch.randn(batch_size, max_len, dim)   # b, max_len, dim
    layer_norm = nn.LayerNorm(dim, elementwise_affine=False)

    out = layer_norm(x)
    print("out: ", out, out.shape)

    # 自定义求结果
    eps = 0.00001
    mean = torch.mean(x[:, :, :], dim=(-1), keepdim=True)
    var = torch.square(x[:, :, :] - mean).mean(dim=(-1), keepdim=True)
    out_ = (x[:, :, :] - mean) / torch.sqrt(var + eps)

    print("mean: ", mean.shape)
    print("var: ", var.shape)
    print("out_: ", out_)



def huggingface_using():
    encoded_inputs = tokenizer(
        text='股东大汇今天召开了',   # [cls] text [sep] text_pair [cls]
        text_pair='学历',
        truncation=True,
        max_length=20,
        add_special_tokens=True)

    print(encoded_inputs)
    print(tokenizer.encode('学历'))
    print(tokenizer.decode([1, 18, 382, 2]))



def test_param(model):
    decay_params = [
        p.name for n, p in model.named_parameters()
        if not any(nd in n for nd in ["bias", "norm"])
    ]
    print(decay_params)



if __name__ == '__main__':
    model_path = "../../bert-base-chinese"
    config = AutoConfig.from_pretrained(model_path)
    model = AutoModel.from_pretrained(model_path, config=config)
    tokenizer = BertTokenizer.from_pretrained(model_path)


    # count_model_params(model)
    # check_model(model)
    # forward_bert()

    # test_layer_norm()

    # huggingface_using()

    test_param(model)

