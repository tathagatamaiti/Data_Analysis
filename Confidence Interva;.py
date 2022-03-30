import numpy as np
from scipy.stats import t
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

#loading the data
mydata1= pd.read_csv("C:\\Internship\\datasets\\out0ms.csv",header = None, names = ['IterationNumber', 'Runtime', 'Sleep time'])
mydata2= pd.read_csv("C:\\Internship\\datasets\\out10ms.csv",header = None, names = ['IterationNumber', 'Runtime', 'Sleep time'])
mydata3= pd.read_csv("C:\\Internship\\datasets\\out50ms.csv",header = None, names = ['IterationNumber', 'Runtime', 'Sleep time'])
mydata4= pd.read_csv("C:\\Internship\\datasets\\out500ms.csv",header = None, names = ['IterationNumber', 'Runtime', 'Sleep time'])

#specifiying the variables
x1 = mydata1.drop('Runtime', axis=1)
y1 = mydata1.Runtime
x2 = mydata2.drop('Runtime', axis=1)
y2 = mydata2.Runtime
x3 = mydata3.drop('Runtime', axis=1)
y3 = mydata3.Runtime
x4 = mydata4.drop('Runtime', axis=1)
y4 = mydata4.Runtime

#calculating the mean
m1 = y1.mean()
print('Mean 1:', m1)
m2 = y2.mean()
print('Mean 2:', m2)
m3 = y3.mean()
print('Mean 3:', m3)
m4 = y4.mean()
print('Mean 4:', m4)

#calculating the standard deviation
s1 = y1.std()
print('Standard Deviation 1:', s1)
s2 = y2.std()
print('Standard Deviation 2:', s2)
s3 = y3.std()
print('Standard Deviation 3:', s3)
s4 = y4.std()
print('Standard Deviation 4:', s4)

#calculating the confidence interval
dof1 = len(y1)-1
dof2 = len(y2)-1
dof3 = len(y3)-1
dof4 = len(y4)-1
confidence = 0.95
t_crit1 = np.abs(t.ppf((1-confidence)/2,dof1))
t_crit2 = np.abs(t.ppf((1-confidence)/2,dof2))
t_crit3 = np.abs(t.ppf((1-confidence)/2,dof3))
t_crit4 = np.abs(t.ppf((1-confidence)/2,dof4))

#printing the confidence interval
print('Lower bound of the interval 1:', m1-s1*t_crit1/np.sqrt(len(y1)), ',' , 'Upper bound of the interval 1:' , m1+s1*t_crit1/np.sqrt(len(y1)))
print('Lower bound of the interval 2:', m2-s2*t_crit2/np.sqrt(len(y2)), ',' , 'Upper bound of the interval 2:' , m2+s2*t_crit2/np.sqrt(len(y2)))
print('Lower bound of the interval 3:', m3-s3*t_crit3/np.sqrt(len(y3)), ',' , 'Upper bound of the interval 3:' , m3+s3*t_crit3/np.sqrt(len(y3)))
print('Lower bound of the interval 4:', m4-s4*t_crit4/np.sqrt(len(y4)), ',' , 'Upper bound of the interval 4:' , m4+s4*t_crit4/np.sqrt(len(y4)))

#concatenating the datasets
alldata = pd.concat([mydata1.assign(dataset='set1'), mydata2.assign(dataset='set2'), mydata3.assign(dataset='set3'), mydata4.assign(dataset='set4')])

#plotting the scatter plot
sns.scatterplot(x='IterationNumber', y='Runtime', hue='Sleep time',  data=alldata, palette=['black','green', 'orange', 'blue'], legend='full' )
plt.show()






