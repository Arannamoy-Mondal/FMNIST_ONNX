import torch 
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader,Dataset
import time
import pandas as pd 
import numpy as np 

class CustomDataset(Dataset):
    def __init__(self,csv_file):
        data=pd.read_csv("dataset/fashion-mnist_test.csv")

