import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

sns.set_style('whitegrid')
palette = sns.color_palette('dark:#5B9_r')
sns.set_palette(palette=palette)

class BivariateAnalysis:
    def __init__(self):
        self.df = pd.read_csv(r'Classification-of-Wheat-Varieties\datasets\sampled.csv')
        self.df = self.df.iloc[:,1:]
        self.features = self.df.columns
    
    def __cov(self):
        self.cov = self.df.cov(numeric_only=True)
        self.cov.to_csv(r'Classification-of-Wheat-Varieties\output\df\bivariate_metrics\cov_matrix.csv')
        
    def __corr(self):
        self.corr = self.df.corr(numeric_only=True)
        self.corr.to_csv(r'Classification-of-Wheat-Varieties\output\df\bivariate_metrics\corr.csv')
    
    def __kde(self):
        fig,axes = plt.subplots(1,4,figsize=(25,4),squeeze=False)
        fig.suptitle('KDE Plots')
        for i in range(4):
            x = self.features[i]
            y= self.features[-1-i]
            sns.kdeplot(data=self.df,x=x,y=y,ax=axes[0][i])
            axes[0][i].set_title(f'Kde for {x}, {y}')
        plt.tight_layout()
        plt.savefig(r'Classification-of-Wheat-Varieties\output\plots\kde_plot.png')
    
    def __scatterplot(self):
        fig,axes = plt.subplots(8,8,figsize=(25,25),squeeze=False)
        fig.suptitle('Scatter Plot')
        hue = self.df.Label
        for i in range(8):
            for j in range(8):
                x=self.features[i]
                y=self.features[j]
                sns.scatterplot(data=self.df,x=x,y=y,hue=hue,palette=palette,ax=axes[i][j])
                axes[i][j].set_title(f'Scatter plots for {x},{y}')
        
        plt.tight_layout()
        plt.savefig(r'Classification-of-Wheat-Varieties\output\plots\scatterplot.png')
    
    def __heatmap(self):
        plt.figure(figsize=(10,10))
        plt.title('Heat Map')
        sns.heatmap(data=self.corr,center=0,annot=True,fmt='.2f',linewidths=0.5,linecolor='black',vmin=-0.58,vmax=1,cmap='crest')
        plt.savefig(r'Classification-of-Wheat-Varieties\output\plots\heatmap.png')


    def bivariate_analysis(self):
        self.__cov()
        self.__corr()
        self.__kde()
        self.__scatterplot()
        self.__heatmap()
        
            
if __name__ == '__main__':
    bv = BivariateAnalysis()
    bv.bivariate_analysis()