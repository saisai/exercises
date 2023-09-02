from matplotlib import pyplot as plt
import seaborn as sns
df = sns.load_dataset('car_crashes')
plt.scatter(df.speeding,df.alcohol)
sns.set()
plt.show()
