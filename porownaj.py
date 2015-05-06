#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import string
#import numpy as np
import csv
import urllib
import os, errno
import difflib


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def fetch_pdb(id, kat):
  mkdir_p(kat)
  url = 'http://www.rcsb.org/pdb/files/%s.pdb' % id
  pdb = urllib.urlopen(url).read()
  outfile = open(kat + "/" + id + ".pdb", "w")
  outfile.write(pdb)
  outfile.close()

lista = {}

with open('RNA-bezlig-oneline.txt', 'rb') as rna1Csvfile:
  rna = csv.reader(rna1Csvfile, delimiter='\t')
  for seq in rna:
    with open('RNA+lig-oneline.txt', 'rb') as rna2Csvfile:
      rnalig = csv.reader(rna2Csvfile, delimiter='\t')
      for seqlig in rnalig:
	#if (seq[0] != seqlig[0] and seqlig[4] == seq[4] and len(seqlig[4])>15): #-- identyczne
	#if (seq[0] != seqlig[0] and (seqlig[4] in seq[4] or seq[4] in seqlig[4]) and seq[4] != seqlig[4] and len(seq[4])>25 and len(seqlig[4])>25): # nieidentyczne - ligandowa sekwencja w apo albo odwrotnie
	#podobienstwo
	diff=difflib.SequenceMatcher(None, seqlig[4], seq[4])
	podob = float(diff.ratio())
	#print podob
	#if (seq[0] != seqlig[0] and podob > 0.8 and seq[4] != seqlig[4] and len(seq[4])>25 and len(seqlig[4])>25): # nieidentyczne - ligandowa sekwencja w apo albo odwrotnie
	if (seq[0] != seqlig[0] and podob <= 0.8 and podob > 0.7 and seq[4] != seqlig[4] and len(seq[4])>25 and len(seqlig[4])>25): # nieidentyczne - ligandowa sekwencja w apo albo odwrotnie
	  if seq[0] not in lista: lista[seq[0]] = []
	  lista[seq[0]].extend([seqlig[0]])
	  print seq[0], seqlig[0]


print lista

for apo in lista:
  #print apo, lista[apo]
  print apo, "::",
  fetch_pdb(apo, apo)
  for zlig in lista[apo]:
    print zlig,
    fetch_pdb(zlig, apo)
  print ""
