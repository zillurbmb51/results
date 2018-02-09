import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st=pd.read_csv("Statistics_PerSpecies.csv",index_col=0)
sns.heatmap(s4,annot=True,cmap='Set3',fmt="",linewidths=0.1,robust=True,annot_kws={"size":6,"rotation":'vertical'},alpha=1.0)
plt.savefig("all_stat_heat_fin_1.png",bbox_inches='tight')

sp=pd.read_csv("Orthogroups_SpeciesOverlaps.csv",sep="\t",index_col=0)

a5=sns.clustermap(sp,cmap="spectral_r")
a5.savefig("species_overlap.png")

s3=sp.set_index('VbrassicaformisCCMP3155')
a7=sns.clustermap(s3,cmap="spectral_r")
a7.savefig("species_overlap_vbras.png")
s4=sp.set_index('CveliaCCMP2878')
a8=sns.clustermap(s4,cmap="spectral_r")
a8.savefig("species_overlap_cveli.png")
