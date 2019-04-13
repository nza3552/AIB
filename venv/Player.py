
import pygame
import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple
from itertools import count
from PIL import Image

import io
import torch
import torchvision
import torch.utils.data
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T
from AI import AI
from threading import Thread
import threading
import time

is_ipython = 'inline' in matplotlib.get_backend()
plt.ion()
device = torch.device("cpu")
machine = AI()
iterations = 100


class Player():
    def __init__(self, pool):
        self.pool = pool

    def startMachine(self):
        print("HERE")
        time.sleep(1)
        pygame.image.save(self.pool.table.screen, "stage.jpg")
        image = Image.open("stage.jpg")
        print(image.size)
        print(image.mode)
        image.show()

# def main():
#     # thread = Thread(target=pool.play)
#     thread2 = Thread(target=startMachine)
#     thread2.start()
#     # thread.start()
#     # while iterations > 1:
#     # if pool.ready:


