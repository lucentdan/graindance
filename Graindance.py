
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib notebook')

from scipy.io.wavfile import write
from numpy import linspace,sin,pi,int16,concatenate
from pylab import plot,show,axis

import pandas as pd
import os
from os.path import isfile, join 


# In[2]:

fileList = os.listdir('gg/')

def isDataFile(filename):
    return filename.find('.dat')>0

dataFiles = filter(isDataFile,fileList)


# In[5]:

len(dataFiles)


# In[4]:

pd.read_csv('gg/'+dataFiles[0],sep='\t',header=None,names=('grain-ID','area','sides'))


# In[2]:

# tone synthesis
def note(freq, len, amp=1, rate=44100):
 t = linspace(0,len,len*rate)
 data = sin(2*pi*freq*t)*amp
 return data.astype(int16) # two byte integers


# In[10]:

# A tone, 2 seconds, 44100 samples per second

tone_1 = note(440,2,amp=10000) + note(660,2,amp=10000)
tone_2 = note(440,2,amp=10000)

tone_total = concatenate((tone_1,tone_2))

write('test.wav',44100,tone_total) # writing the sound to a file

#plot(linspace(0,2,2*44100),tone_total)
#axis([0,0.4,15000,-15000])
#show()


# In[ ]:



