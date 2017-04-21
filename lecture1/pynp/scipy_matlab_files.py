#!python27
# octave save_a.m
# save matric to octave_a.mat
#
import scipy.io as sio
ma = sio.loadmat("octave_a.mat")
print ma['a'] #wrong
print "----------"
