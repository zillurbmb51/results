#This script will calculate GC content of all the fasta file in a directory persequence and per file
#The 1st line will give GC content persequence
#The 2nd line will give mean GC for a file
#Run : bash gc_avg.sh

for f in *fasta; do bioawk -c fastx '{print $name, gc($seq)}' $f > $f.gc; done
for f in *gc; do awk '{ total +=$2 } END { print total/NR }' $f > $f.avg; done
#rm *gc
