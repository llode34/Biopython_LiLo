#!/usr/bin/env python

from SeqRecord import *
from seq import *

if (__name__ == '__main__'):
	fasta_filename = "NC_005816.fna"
	record=my_read_function(fasta_filename, "fasta")
	print get_GC_content(record.seq)
	gb_filename="NC_005816.gb"
	genbank_record=my_read_function(gb_filename, "genbank")
	print genbank_record.features
