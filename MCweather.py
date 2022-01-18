# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 21:46:45 2021

@author: Izat
"""


import numpy as np
from numpy.linalg import matrix_power

events = ['rainy', 'sunny', 'cloudy']

transition = np.array([[0.5, 0.25, 0.25], [0.5, 0, 0.5], [0.25, 0.25, 0.5]])

rain_ = np.array([1, 0, 0])
sun_ = np.array([0, 1, 0])
cloud_ = np.array([0, 0, 1])

sun_pred = sun_.dot(matrix_power(transition, 7))



#evals, evecs = np.linalg.eig(transition.T)
#evec1 = evecs[:,np.isclose(evals, 1)]

#evec1 = evec1[:,0]

#stationary = evec1 / evec1.sum()

#stationary = stationary.real
stationary = []
i = 1
while True:
  sun_pred_1 = sun_.dot(matrix_power(transition, i))
  sun_pred_2 = sun_.dot(matrix_power(transition, i+2))
  stationary = sun_pred_2
  if(all(sun_pred_1 == sun_pred_2)):
    break
  i+=1



print(stationary)

#stationary distribution
#talk about rock reconstruction (porosity, permeability)