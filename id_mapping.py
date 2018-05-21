#This script will map different types of id from a mapping table
import pandas as pd #Import libraries
import numpy as np
import seaborn as sns
o11=pd.read_csv("Orthogroups.csv",sep='\t',index_col=0) #Load the data
idg=pd.read_csv("id_to_go.csv") #Mapping table generated from bioconductor database
o11['Pfalciparum3D7'].isnull().values.sum() #Count number of missing data in a column
idg2=idg[pd.notnull(idg['GO'])] #Create a new dataframe excluding missing values from a certain column
d11=dict(zip(idg2.SYMBOL,idg2.GO)) #Create dictionary to map 
o11['go']=o11['Pfalciparum3D7'].str.extract('('+'|'.join(list(d11))+')').map(d11) #Create new column mapping with dictionary 
o13=o11[pd.notnull(o11['go'])]
d13=dict(zip(o13.index,o13.go)) #Create dictionary with index and another column
gncnt=pd.read_csv("Orthogroups.GeneCount.csv",sep='\t',index_col=0)
gc=gncnt.drop(['Total'],axis=1) #Drop a certain column
gc2=gc.assign(orthogroups=gc.index) #Create a new column with orthogroups name
gc2['go']=gc2['orthogroups'].map(d13)
gc3=gc2[pd.notnull(gc2['go'])]
gtp=pd.read_csv("go_to_path.csv") #Load the corresponding GO IDs and K number dataframe
gtp2=gtp[pd.notnull(gtp["PATH"])]
d15=dict(zip(gtp2.GO,gtp2.PATH))
gc3['path']=gc3['go'].map(d15)
gc4=gc3[pd.notnull(gc3['path'])]
kegg=pd.read_csv("kegg_4.csv") #Load the K number and pathway name
kegg.columns=['path','pathway'] #Naming columns
kegg['pathway']=kegg['pathway'].map(str.strip) #remove extra white spaces from strings
kegg2=kegg[pd.notnull(kegg['path'])]
d17=dict(zip(kegg2.path,kegg2.pathway))
gc4['pathway']=gc4['path'].map(d17)
gc5=gc4.drop(['orthogroups','go','path'],axis=1) 
gc6=gc5.groupby(['pathway']).sum() #Tidy data for next step of analysis
gc6.to_csv("pathway_count.csv")
sns.clustermap(gc6,cmap="nipy_spectral_r") #Hierarchical clustering
plt.savefig("pathway_cluster.svg",bbox_inches='tight')
