source("http://bioconductor.org/biocLite.R") #Load bioconductor
biocLite("org.Pf.plasmo.db") #Install the p. falciparum databse
library(org.Pf.plasmo.db) #Load the database
ls("package:org.Pf.plasmo.db") #List available options
ids <- keys(org.Pf.plasmo.db, "SYMBOL") #Create a list with gene symbols
id_to_go=select(org.Pf.plasmo.db, ids, "GO", keytype="SYMBOL") #Create a datframe of corresponding symbol and GO
write.csv(id_to_go,"id_to_go.csv") #Write the mapping file to csv
gos=keys(org.Pf.plasmo.db,"GO") #Create a list with GO IDs
go_to_path=select(org.Pf.plasmo.db, gos,"PATH",keytype="GO") #Create dataframe of corresponding GO and K number
write.csv(go_to_path,"go_to_path.csv")
