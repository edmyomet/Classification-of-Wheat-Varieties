import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as mpl
import seaborn as sns
import scipy.stats as stats

sns.set_style('whitegrid')
palette = sns.color_palette('dark:#5B9_r')
sns.set_palette(palette=palette)
class UnivariateAnalysis:
    def __init__(self):
        self.df = pd.read_csv(r'Classification-of-Wheat-Varieties\datasets\sampled.csv')
        self.df = self.df.iloc[:,1:]
        self.features = self.df.columns
        print(self.features)
    
    def __descr(self):
        self.df.describe().to_csv(r'Classification-of-Wheat-Varieties\output\df\univariate_metrics\dataset_description.csv')
    
    def __mean(self):
        self.mean = self.df.mean(numeric_only=True,skipna=True)
        self.mean.to_csv(r'Classification-of-Wheat-Varieties\output\df\univariate_metrics\mean.csv')
    
    def __median(self):
        self.median = self.df.median(numeric_only=True, skipna=True)
        self.median.to_csv(r'Classification-of-Wheat-Varieties\output\df\univariate_metrics\median.csv')
        
    def __freq(self):
        pass

    def __mode(self):
        self.mode = self.df.mode(numeric_only=True)
        self.mode.to_csv(r'Classification-of-Wheat-Varieties\output\df\univariate_metrics\mode.csv')
    
    def __std(self):
        self.std = self.df.std(numeric_only=True)
        self.std.to_csv(r'Classification-of-Wheat-Varieties\output\df\univariate_metrics\std.csv')
    
    def __skew(self):
        self.skew = self.df.skew(numeric_only=True)
        self.skew.to_csv(r'Classification-of-Wheat-Varieties\output\df\univariate_metrics\skew.csv')
    
    def __kurt(self):
        self.kurt = self.df.kurtosis(numeric_only=True)
        self.kurt.to_csv(r'Classification-of-Wheat-Varieties\output\df\univariate_metrics\kurtosis.csv')
    
    def __boxplot(self):
        fig,axes = plt.subplots(1,7,figsize=(35,8),squeeze=False)
        fig.suptitle('BoxPlots for Outlier Detection')
        for i in range(7):
            try:
                feature = self.features[i]
                sns.boxplot(data=self.df,y=feature, width=0.2, ax=axes[0][i])
                axes[0][i].set_title(f'BoxPlot for {self.features[i]}')
            except:
                pass
        plt.tight_layout()
        plt.savefig(r'Classification-of-Wheat-Varieties\output\plots\boxplot.png')
        
    
    def __normal_distr(self):
        fig,axes=plt.subplots(1,7,figsize=(35,8),squeeze=False)
        fig.suptitle('Normal Distribution Curve for Attributes')
        for i in range(7):
            feature = self.features[i]
            sns.histplot(data=self.df, x=feature,kde=True,ax=axes[0][i]).lines[0].set_color('black')
            axes[0][i].set_title(f'{self.features[i]}')
        plt.tight_layout()
        plt.savefig(r'Classification-of-Wheat-Varieties\output\plots\normal_distr.png')
    
    def __outlier_remove(self):
        for feature in self.features:
            q1 = self.df[feature].quantile(0.25)
            q3 = self.df[feature].quantile(0.75)
            iqr = q3 - q1
            
            lower = q1 - 1.5*iqr
            upper = q3 + 1.5 * iqr
            
            self.df_cleaned = self.df[(self.df[feature] > lower) & (self.df[feature] < upper)]
            self.df = self.df_cleaned
    def univariate_analysis(self):
        self.__descr()
        self.__mean()
        self.__median()
        self.__mode()
        self.__std()
        self.__skew()
        self.__kurt()
        self.__boxplot()
        self.__normal_distr()
        self.__outlier_remove()
    
    
            

if __name__ == '__main__':
    uv = UnivariateAnalysis()
    uv.univariate_analysis()
        