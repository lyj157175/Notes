from transformers import BertPreTrainedModel, BertModel, PretrainedConfig
from transformers import BertTokenizer, BertTokenizerFast
import torch
import torch.nn as nn
from typing import Optional


class MyBert(BertPreTrainedModel):

    def __init__(self, config: PretrainedConfig):
        super(MyBert, self).__init__(config)
        self.bert = BertModel(config)
        self.config = config
        self.hidden_size = self.config.hidden_size

        self.fc_start = nn.Linear(self.hidden_size, 1)
        self.fc_end = nn.Linear(self.hidden_size, 1)
        self.sigmoid = nn.Sigmoid()


    def forward(self, input_ids = None,
                token_type_ids = None,
                position_ids = None,
                attention_mask = None,
                head_mask = None,
                inputs_embeds = None,
                start_positions = None,
                end_positions = None,
                output_attentions = None,
                output_hidden_states = None,
                return_dict = None
                ):
        outputs = self.bert(
            input_ids=input_ids,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            attention_mask=attention_mask,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict
        )
        sequence_output = outputs[0]

        start_logits = self.fc_start(sequence_output)
        start_logits = torch.squeeze(start_logits, -1)
        start_prob = self.sigmoid(start_logits)
        end_logits = self.fc_end(sequence_output)
        end_logits = torch.squeeze(end_logits, -1)
        end_prob = self.sigmoid(end_logits)

        total_loss = None
        if start_positions is not None and end_positions is not None:
            loss_fct = nn.BCELoss()
            start_loss = loss_fct(start_prob, start_positions)
            end_loss = loss_fct(end_prob, end_positions)
            total_loss = (start_loss + end_loss) / 2.0

        output = (start_prob, end_prob) + outputs[2:]
        return total_loss if total_loss else (start_prob, end_prob)



if __name__ == "__main__":
    model_path = 'data/uie_base_pytorch'    # 模型名字
    tokenizer = BertTokenizerFast.from_pretrained(model_path)
    model = BertModel.from_pretrained(model_path)
    # print(model)

    my_bert = MyBert.from_pretrained(model_path)
    print(my_bert.hidden_size)

