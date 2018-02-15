import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
pt=pd.read_csv("pathway_count.csv",index_col=0)
pt1=pt.drop(['proteome size'])
sns.clustermap(pt1,cmap="nipy_spectral_r")
plt.show()
plt.savefig("pathway_cluster.svg",bbox_inches='tight')
