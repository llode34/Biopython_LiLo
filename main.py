#!/usr/bin/env python

#import all qui est dans le fichier seqrecord
from seqrecord import *
from seq import *
if __name__== "__main__":
    filename="NC_005816.fna"
    fasta_record=my_read_function(filename,"fasta")
    print get_GC_content(fasta_record.seq)
    gb_filename="NC_005816.gb"
    gb_record=my_read_function(gb_filename,"genbank")
    for feature in gb_record.features:
        print feature.type
        print feature.location


    

#GC est egal au %de GC dans une sequence donne





