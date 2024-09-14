import pandas
import matplotlib
import scipy
import seaborn as sns
print(sns.get_dataset_names())

df = sns.load_dataset('car_crashes')
print(df.head())

print('\n')
from matplotlib import pyplot as plt
import seaborn as sns
plt.scatter(df.speeding,df.alcohol)
plt.show()
