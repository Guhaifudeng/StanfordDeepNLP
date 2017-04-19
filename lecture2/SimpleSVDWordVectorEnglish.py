#!python27
# -*- coding: utf-8 -*-
'''
Window based cooccurence matrix
Dimensionality Reduction on X
Simple SVD word vectors in Python

Corpus:
I like deep learning.
I like NLP.
I enjoy flying.


'''
import numpy as np
from numpy import *
la = np.linalg
words = ["I", "like", "enjoy", "deep", "learning", "NLP", "flying ", "." ]
X = np.array([
    [0,2,1,0,0,0,0,0],
    [2,0,0,1,0,1,0,0],
    [1,0,0,0,0,0,1,0],
    [0,1,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,1],
    [0,1,0,0,0,0,0,1],
    [0,0,1,0,0,0,0,1],
    [0,0,0,0,1,1,1,0]
    ])
U, s, Vh = la.svd(X, full_matrices = False)
print shape(U),shape(s),shape(Vh)# s 为对角矩阵
#Printing first two columns of U corresponding to the 2 biggest singular values
#why ? 能否做个三维的？
import matplotlib.pyplot as plt
for i in range(len(words)):
    print U[i,0], U[i,1], words[i]
    plt.text(U[i,0], U[i,1], words[i])
plt.axis([-0.8, 0.2, -0.8, 0.8])#必须设置，默认[0,1,0,1]
plt.show()
