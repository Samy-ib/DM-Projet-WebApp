import torch
import torch.nn as nn
import torch.nn.functional as F

class Net_NSP(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(20,80)
        self.fc2 = nn.Linear(80,160)
        self.fc3 = nn.Linear(160,320)
        self.fc4 = nn.Linear(320,160)
        self.fc5 = nn.Linear(160,80)
        self.fc6 = nn.Linear(80,3)




        self.dropout = nn.Dropout(p=0.25)

    def forward(self, X):
        X = self.dropout(F.gelu(self.fc1(X)))
        X = self.dropout(F.gelu(self.fc2(X)))
        X = self.dropout(F.gelu(self.fc3(X)))
        X = self.dropout(F.gelu(self.fc4(X)))
        X = self.dropout(F.gelu(self.fc5(X)))


        X = F.softmax(self.fc6(X), dim = 1)

        return X

def normaliseRow(row):
    """
        Normalise one row only(for prediction)
    """
    maxMin=[[106, 160], [0, 26], [0, 564], [0, 23], [12, 87], [0.2, 7.0], [0, 91], [0.0, 50.7], [0, 16], [0, 1], [0, 4], [3, 180], [50, 159], [122, 238], [0, 18], [0, 10], [60, 187], [73, 182], [77, 186], [0, 269]]
    for i in range(len(row)):
        row[i] = (row[i] - maxMin[i][0]) / (maxMin[i][1] - maxMin[i][0])
    
    return row

def predict(row):
    """
        Given the model and a list containing the attribute
        we predict the NSP class.
    """
    row = normaliseRow(row)
    row = torch.FloatTensor(row)
    row = row.unsqueeze(0) #getting rid of "IndexError: Dimension out of range (expected to be in range of [-1, 0], but got 1)" due to missing batch dimension
    network = loadNet('app/api/nsp_model.pt')
    out = network(row)
    # print(out[0].max[0])
    probs = [float(i) for i in out[0]]
    ind = int(out[0].max(0)[1])
    return ind,probs

def loadNet(path):
    network = Net()
    network.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
    return network