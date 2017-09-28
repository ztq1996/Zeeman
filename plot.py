'''
Created on Sep 26, 2017

@author: zhangtianqing
'''


import matplotlib.pyplot as plt
import numpy as np
import scipy

mercury_green_dn_val=[0.161,0.183,0.206,0.236]
mercury_green_dn_err=[0.017,0.019,0.017,0.036]
mercury_green_B_val=[0.343,0.384,0.424,0.465]
mercury_green_B_err=[]


plt.errorbar(mercury_green_B_val,mercury_green_dn_val,mercury_green_dn_err)
plt.show()


