# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

facebook = pd.read_csv('FB Historical Data.csv',usecols = [0,1,2,3,4])

POHL_avg = facebook[['Price','Open','High','Low']].mean(axis = 1)


obs = np.arange(1,len(facebook)+1,1)

plt.plot(obs,POHL_avg,'r',label = 'MY FIRST PLOT')











