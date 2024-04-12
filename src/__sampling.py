import numpy as np
import pandas as pd
import matplotlib.pylab as mpl
import matplotlib.pyplot as plt

class StratifiedSample:
    def __init__(self):
        self.df = pd.read_csv(r'Classification-of-Wheat-Varieties\datasets\seeds_dataset.csv',sep='\t+',header=None)
        self.df.columns = ['Area','Perimeter','Compactness','KernelLength','KernelWidth','AsymmetryCoef','KernelGrooveLength','Label']
    
    def __sample(self):
        self.sample = self.df.groupby('Label',group_keys=False).apply(lambda x: x.sample(min(len(x),20)))
        self.sample.index = [None] * 60
        self.sample.to_csv(r'Classification-of-Wheat-Varieties\datasets\sampled.csv')
        
    
    def sample(self):
        self.__sample()



if __name__ == '__main__':
    ss = StratifiedSample()
    ss.sample()