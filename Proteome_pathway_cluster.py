#This script will create a hierarchical cluster map from abundance data
#To run: python Proteome_pathway_cluster.py ; in the same directory of the data set
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns #Load needed libraries
pt=pd.read_csv("pathway_count.csv",index_col=0) #Load the data
pt1=pt.drop(['proteome size']) #Drop unwanted columns
sns.clustermap(pt1,cmap="nipy_spectral_r") #Make the plot
plt.savefig("pathway_cluster.svg",bbox_inches='tight') #Save it aand then show and close
plt.show()
plt.close()
