import numpy as np
import pandas as pd
import matplotlib.pylab as mpl
import matplotlib.pyplot as plt
import seaborn as sns


class ExpectedValues:
     def __init__(self):
        self.df = pd.read_csv(r'Classification-of-Wheat-Varieties\datasets\seeds_dataset.csv',sep='\t+',header=None)
        self.df.columns = ['Area','Perimeter','Compactness','KernelLength','KernelWidth','AsymmetryCoef','KernelGrooveLength','Label']
        self.features = self.df.columns

if __name__ == '__main__':
    ev = ExpectedValues()