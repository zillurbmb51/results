import pandas as pd #Import libraries
import numpy as np
o11=pd.read_csv("Orthogroups.csv",sep='\t',index_col=0) #Load the data
idg=pd.read_csv("id_to_go.csv") #Mapping table generated from bioconductor database
o11['Pfalciparum3D7'].isnull().values.sum() #Count number of missing data in a column
idg2=idg[pd.notnull(idg['GO'])] #Create a new dataframe excluding missing values from a certain column
d11=dizt(zip(idg2.SYMBOL,idg2.GO)) #Create dictionary to map 
o11['go']=o11['Pfalciparum3D7'].str.extract('('+'|'.join(list(d11))+')').map(d11) #Create new column mapping with dictionary 
o13=o11[pd.notnull(o11['go'])]
d13=dict(zip(o13.index,o13.go)) #Create dictionary with index and another column
gncnt=pd.read_csv("Orthogroups.GeneCount.csv",sep='\t',index_col=0)
gc=gncnt.drop(['Total'],axis=1) #Drop a certain column
gc2=gc.assign(orthogroups=gc.index)
gc2['go']=gc2['orthogroups'].map(d13)
gc3=gc2[pd.notnull(gc2['go'])]
