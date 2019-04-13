import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple
from itertools import count
from PIL import Image

import torch
import torch.utils.data
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T



class AI(nn.Module):
    def __init__(self):
        super(AI, self).__init__()

        self.number_of_actions = 2
        self.gamma = 0.99# i dont' use any of these yet...?
        self.final_epsilon = 0.0001
        self.initial_epsilon = 0.1
        self.number_of_iterations = 2000000
        self.replay_memory_size = 10000
        self.minibatch_size = 32

        self.conv1 = nn.Conv1d(450, 225, 426)
        self.relu1 = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv1d(225, 100, 201)
        self.relu2 = nn.ReLU(inplace=True)
        # self.conv3 = nn.Conv1d(100, 64, 4, 4)
        # self.relu3 = nn.ReLU(inplace=True)
        self.fc4 = nn.Linear(90000, 512)
        self.relu4 = nn.ReLU(inplace=True)
        self.fc5 = nn.Linear(512, self.number_of_actions)

    def forward(self, x):
        out = self.conv1(x)
        out = self.relu1(out)
        out = self.conv2(out)
        out = self.relu2(out)
        # out = self.conv3(out)
        # out = self.relu3(out)
        out = out.view(1, -1)
        out = self.fc4(out)
        out = self.relu4(out)
        out = self.fc5(out)
        return out








#fuck idk
# Transition = namedtuple('Transition',
#                         ('state', 'action', 'next_state', 'reward'))
# class ReplayMemory(object):
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.memory = []
#         self.position = 0
#
#     def push(self, *args):
#         if len(self.memory) < self.capacity:
#             self.memory.append(None)
#         self.memory[self.position] = Transition(*args)
#         self.position = (self.position + 1) % self.capacity
#
#         def sample(self, batch_size):
#             return random.sample(self.memory, batch_size)
#
#         def __len__(self):
#             return len(self.memory)
#https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html