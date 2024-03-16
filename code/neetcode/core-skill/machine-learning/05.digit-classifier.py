import torch
import torch.nn as nn
from torchtyping import TensorType

# https://neetcode.io/problems/handwritten-digit-classifier
class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        self.first_layer = nn.Linear(784, 512)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.2)
        self.output_layer = nn.Linear(512, 10)
        self.sigmoid = nn.Sigmoid()
        pass
        # Define the architecture here

    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        return self.sigmoid(
            self.output_layer(self.dropout(self.relu(self.first_layer(images))))
        )
        pass
        # Return the model's prediction to 4 decimal places

model = Solution()

loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

epochs = 5
for epoch in range(epochs):
    for images, labels in train_dataloader:
        images = images.view(images.shape[0], 784)

        #TRAINING BODY
        model_predict = model(images)
        optimizer.zero_grad()
        loss = loss_function(model_predict, labels)
        loss.backward()
        optimizer.step()