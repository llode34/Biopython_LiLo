#!usr/bin/env python

from Bio.Seq import Seq
from Bio.SeqUtils import GC

def get_GC_content(seq):
	return GC(seq)

def get_length(seq):
	return len(seq)
	
