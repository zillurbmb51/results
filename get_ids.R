source("http://bioconductor.org/biocLite.R")
biocLite(org.Pf.plasmo.db)
library(org.Pf.plasmo.db) #First 3 lines are for install and load the package
ls("package:org.Pf.plasmo.db") #List available options
ids <- keys(org.Pf.plasmo.db, "SYMBOL") #Create a list with desired key
id_to_go=select(org.Pf.plasmo.db, ids, "GO", keytype="SYMBOL") #Create a datframe with corresponding keys and values
write.csv(id_to_go,"id_to_go.csv") #Write the mapping file to csv
