from matplotlib import pyplot as plt
import seaborn as sns
df = sns.load_dataset('car_crashes')
plt.scatter(df.speeding,df.alcohol)
#sns.set()
#sns.set_style('whitegrid')
#sns.set_style('dark')
sns.set_style("ticks")
sns.despine()
plt.show()
