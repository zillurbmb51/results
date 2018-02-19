library(dendextend)
phyl1=read.csv("mega/d3.csv",row.names=1,header=F) #Phylogenomic distance from mega
phyl1[is.na(phyl1)]<-0 #Replace NA with 0
dphylo=as.dendrogram(hclust(dist(phyl1))) #Create dendrogram of hierarchical cluster
ortho=read.csv("Orthogroups_SpeciesOverlaps.csv",sep='\t',row.names=1)
dortho=as.dendrogram(hclust(dist(ortho)))
path=read.csv("pathway_count.csv",row.names=1)
dpath=as.dendrogram(hclust(dist(t(path))))
dphylortho=dendlist(dphylo,dortho) #Create dendrogram list
dpathortho=dendlist(dpath,dortho)
dphylopath=dendlist(dphylo,dpath)
svg("tangle_phylo_ortho.svg") #Plot the tangle gram
dphylortho %>% untangle(method='step2side') %>% tanglegram(common_subtrees_color_branche = T,margin_inner=10,main = paste("entanglement =", round(entanglement(phylortho), 2)),main_left='Phylogenomic',main_right='Orthogroups',margin_outer=3,sort=F,highlight_distinct_edges = T, highlight_branches_lwd = T)
dev.off()
svg("tangle_path_ortho.svg")
dpathortho %>% untangle(method='step2side') %>% tanglegram(common_subtrees_color_branche = T,margin_inner=10,main = paste("entanglement =", round(entanglement(pathortho), 2)),main_left='Pathway',main_right='Orthogroups',margin_outer=3,sort=F,highlight_distinct_edges = T, highlight_branches_lwd = T)
dev.off()
svg("tangle_phylo_path.svg")
dphylopath %>% untangle(method='step2side') %>% tanglegram(common_subtrees_color_branche = T,margin_inner=10,main = paste("entanglement =", round(entanglement(phylopath), 2)),main_left='Phylogenomic',main_right='Pathway',margin_outer=3,sort=F,highlight_distinct_edges = T, highlight_branches_lwd = T)
dev.off()
#Statistical relationships among dendrograms
all.equal(dphylortho)
all.equal(dphylopath)
all.equal(dpathortho)
cor_bakers_gamma(dphylortho)
cor_bakers_gamma(dphylopath)
cor_bakers_gamma(dpathortho)

