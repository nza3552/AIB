from Pool import Pool

import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple
from itertools import count
from PIL import Image

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T




def main():
    pool = Pool()
    is_ipython = 'inline' in matplotlib.get_backend()
    # if is_ipython:
    #     from IPython import display
    plt.ion()
    device = torch.device("cpu")

class ReplayMemory(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.position = 0

    def push(self, *args):

#https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html