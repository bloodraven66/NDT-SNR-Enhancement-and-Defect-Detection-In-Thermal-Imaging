import torch.nn as nn
import torch.nn.functional as F


class LSTM(nn.Module):
    def __init__(self, input, hidden, num_layers, num_classes):
        super(LSTM,self).__init__()
        self.rnn = nn.LSTM(input_size = input_size, hidden_size = hidden, num_layers = num_layers, batch_first = True)
        self.linear = nn.Linear(hidden, num_classes)
    def forward(self,x):
        r_in = x.view(x.shape[0], 1, x.shape[1])
        r_out, (h_n, h_c) = self.rnn(r_in)
        r_out2 = self.linear(r_out[:, -1, :])
        return F.log_softmax(r_out2, dim=1)
