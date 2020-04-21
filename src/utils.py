import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, TensorDataset
from torch.autograd import Variable
import numpy as np
import scipy.io as spio
import os
from os.path import dirname, join as pjoin
from numpy import array
import random
from matplotlib import pyplot as plt
from IPython.display import clear_output
from collections import Counter
import seaborn as sns
import glob
import matplotlib.ticker as ticker
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from tqdm import tqdm_notebook as tqdm
from sklearn.metrics import f1_score
from IPython.display import clear_output

class Load_data():

    def __init__(self):
        self.value = 10

    def load_mat_file(self, name, mat_key, file_path='../data', ):
        """
        Input data is a matrix stored as .mat file. In matlab it was stored as a cell with a key value of
        Key value for file 1 is 'data'
        Key value for file 2 is 'I'
        """

        mat_path = pjoin(file_path, name)
        mat_file = spio.loadmat(mat_path)
        self.cell_data = mat_file[mat_key]

    def __getitem__(self, index):
        
# def remove_edges(data):
#     data_tr2 = np.zeros((250,256,320))
#     data_tr3 = np.zeros((250,220,320))
#     for i in range(0,250):
#         data_tr = np.transpose(data)
#         data_tr2[i] = np.transpose(data_tr[i])
#         data_tr3[i] = data_tr2[i][20:240]
#     return data_tr3
#
# def non_defected_region_points(data):
#     nd_points = []
#     im = data[10]
#     for i in range(0,220):
#         for j in range(0,320):
#             if(im[i][j]<1.2 and j<45 and j>30):
#                 nd_points.append((i,j))
#                 im[i,j] = 0
#     print(len(nd_points))
#     return nd_points
#
# #second coloumn defected points
# def defected_region_points(data, intensity_thresh=0, x_upper=320, x_lower=0, type='greater', y_lower=0, y_upper=220, time_step=10):
#     d_points = []
#     im = data[time_step]
#     for i in range(0,220):
#         for j in range(0,320):
#           if type=='greater':
#             if(im[i][j]>intensity_thresh and j<x_upper and j>x_lower and i>y_lower and i<y_upper):
#                 d_points.append((i,j))
#                 im[i][j] = 3
#           elif type=='lesser':
#             if(im[i][j]<intensity_thresh and j<x_upper and j>x_lower and i>y_lower and i<y_upper):
#                 d_points.append((i,j))
#                 im[i][j] = 3
#     print(len(d_points))
#     return d_points
# def defected_region_points_fixed(data, irange, jrange, time_step=10, highlight=0.7):
#     d_points = []
#     im = data[time_step]
#     for k in range(len(irange)):
#       irange_, jrange_ = irange[k], jrange[k]
#       for i in range(irange_[0]-20, irange_[1]-20):
#           for j in range(jrange_[0], jrange_[1]):
#                 d_points.append((i,j))
#                 im[i][j] = highlight
#     print(len(d_points))
#     return d_points
# def remove_edges2(data):
#     data_tr = np.zeros((200,256,320))
#     data_tr3 = np.zeros((200,220,320))
#     for i in range(0,200):
#         data_tr[i] = np.transpose(data[i])
#         data_tr3[i] = data_tr[i][20:240]
#
#     return data_tr3
# cell_data4 = remove_edges2(cell_data3)
# cell_data4.shape
#
# #non defected strip between 1st and 2nd coloumn
# def non_defected_region_points2(data):
#     nd_points = []
#     im = data[10]
#     for i in range(0,220):
#         for j in range(0, 320):
#             if(im[i][j]<1.2 and j<45 and j>30):
#                 nd_points.append((i,j))
#                 im[i][j] = 0
#     print(len(nd_points))
#     return nd_points
# test0 = non_defected_region_points2(cell_data4)
# img3 = cell_data4[10]
# plt.imshow(img3)
# plt.show()
# cell_data4 = remove_edges2(cell_data3)
#
# def get_defected_data(d,nd_points,d_points):
#     data = []
#     target = []
#
#     for val in range(len(d_points)):
#
#       d_p = d_points[val]
#       class_ = classes[val+1]
#       for (i,j) in d_p:
#           d1 = []
#           for k in range(200):
#               im = d[k]
#               v = im[i][j]
#               d1.append(v)
#           data.append(d1)
#           target.append([class_])
#     for (i,j) in nd_points:
#         d1 = []
#         for k in range(200):
#             im = d[k]
#             v = im[i][j]
#             d1.append(v)
#         data.append(d1)
#         target.append([0])
#     return data,target
