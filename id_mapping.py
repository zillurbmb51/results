import pandas as pd
import numpy as np
o11=pd.read_csv("Orthogroups.csv",sep='\t',index_col=0)
idg=pd.read_csv("id_to_go.csv")
idg2=idg[pd.notnull(idg['GO'])]
d11=dizt(zip(idg2.SYMBOL,idg2.GO))
o11['go']=o11['Pfalciparum3D7'].str.extract('('+'|'.join(list(d11))+')').map(d11)
o13=o11[pd.notnull(o11['go'])]
d13=dict(zip(o13.index,o13.go))
gncnt=pd.read_csv("Orthogroups.GeneCount.csv",sep='\t',index_col=0)
gc=gncnt.drop(['Total'],axis=1)
gc2=gc.assign(orthogroups=gc.index)
gc2['go']=gc2['orthogroups'].map(d13)
gc3=gc2[pd.notnull(gc2['go'])]
