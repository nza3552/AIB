
import pygame
import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple
from itertools import count
from PIL import Image
from PIL import ImageOps


import io
import torch
import torchvision
import torch.utils.data
import torch.nn
import torch.optim
import torch.nn.functional
from torchvision import transforms
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

    def startMachine(self): ###got it down to two numbers, need to scale it, have it apply them to the game, and then set up training loop
        print("HERE")
        time.sleep(1)
        pygame.image.save(self.pool.table.screen, "stage.jpg")
        image = Image.open("stage.jpg").convert("RGBA")
        image = image.crop((0, 0, 850, 450))
        # print(image.size())
        print(image.size)
        print(image.mode)

        imageTransforms = T.Compose([T.ToTensor()])

        imt = imageTransforms(image)
        # print(imt.size())
        # print(imt.dim())
        # out = machine.forward(imt)
        # print(out.dim())
        # print(out.size())
        # print(out)
        out=machine.forward(imt)
        print(out)



# def main():
#     # thread = Thread(target=pool.play)
#     thread2 = Thread(target=startMachine)
#     thread2.start()
#     # thread.start()
#     # while iterations > 1:
#     # if pool.ready:


