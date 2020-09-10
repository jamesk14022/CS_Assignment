import pandas as pd
import matplotlib.pyplot as plt

file = r'istherecorrelation.csv'
data = pd.read_csv(file, sep=';', header=[0])                               
data.plot(kind='scatter',x='WO [x1000]',y='NL Beer consumption [x1000 hectoliter]')
plt.savefig('output.png', dpi=300)