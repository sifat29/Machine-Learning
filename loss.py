# -*- coding: utf-8 -*-
"""loss

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jgsKwaJ46uX9N-YGD2gdpeMK90HyEhyq
"""

#defining the triplet loss class
class TripletLoss1:
  def __init__(self, margin):
    self.margin = margin
#calculate the loss function of triplet loss          
  def loss(self,anchor, positive, negative):
    positive_distance =torch.sqrt(torch.sum(torch.square(anchor - positive)))
    negative_distance =torch.sqrt(torch.sum(torch.square(anchor - negative)))
    loss1 = ((positive_distance - negative_distance)+ self.margin)
    loss = torch.clip(loss1, 0, None)
    return loss