a1=read.csv("Statistics_Overall_2.csv",skip=24,nrows=14,row.names=1)
a2=read.csv("Statistics_Overall.csv",skip=46,nrows=43,header=T,row.names=1)
png("figure_1.png",width=800,height=700,res=111)
m1 <- matrix(c(1, 1, 2, 3, 4, 5), nrow = 2, byrow = TRUE) #Matrix tamplate for 5 grpahs
layout(m1)
b11=barplot(a2$Number.of.orthogroups,xpd=T,xlab="Number of species in orthogroup",names=1:43,space=0.5,col=c('grey','yellow','pink'),las=2) 
text(b11,a2$Number.of.orthogroups,srt=90,xpd=T,col='black',format(a2$Number.of.orthogroups))
title("Number of orthogroups in all species",adj=0.5,line=-3,sub="A") 
 
nms=c("<1","1","2","3","4","5","6","7","8","9","10","11-15","16-20","21-50") #Selected rows to plot
b12=barplot(a1$Number.of.orthogroups,xpd=T,xlab="Avg. no. of genes per-sp. in orthogroup",names=nms,space=0.5,col=c('grey','yellow','pink'),las=2)
text(b12,a1$Number.of.orthogroups,srt=90,xpd=T,col='black',format(a1$Number.of.orthogroups))
title("Number of orthogroups",adj=0.5,line=-3,sub="B") 
 
b13=barplot(a1$Percentage.of.orthogroups,xpd=T,xlab="Avg. no. of genes per-sp. in orthogroup",names=nms,space=0.5,col=c('grey','yellow','pink'),las=2)
text(b13,a1$Percentage.of.orthogroups,srt=90,xpd=T,col='black',format(a1$Percentage.of.orthogroups))
title("% of orthogroups",adj=0.5,line=-3,sub="C") 
 
b14=barplot(a1$Number.of.genes,xpd=T,xlab="Avg. no. of genes per-sp. in orthogroup",names=nms,space=0.5,col=c('grey','yellow','pink'),las=2)
text(b14,a1$Number.of.genes,srt=90,xpd=T,col='black',format(a1$Number.of.genes))
title("Number of genes",adj=0.5,line=-3,sub="D") 
 
b15=barplot(a1$Percentage.of.genes,xpd=T,xlab="Avg. no. of genes per-sp. in orthogroup",names=nms,space=0.5,col=c('grey','yellow','pink'),las=2) 
text(b15,a1$Percentage.of.genes,srt=90,xpd=T,col='black',format(a1$Percentage.of.genes))
title("% of genes",adj=0.5,line=-3,sub="E") 
dev.off()
