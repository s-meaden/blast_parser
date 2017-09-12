#!/usr/bin/env python

# Script to parse out top hit for batch blast (multifasta) output saved
# in XML format. Use redirect to save output.

# UML class diagram here really useful for choosing what to output:
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#fig:blastrecord


from Bio.Blast import NCBIXML

import sys
inFile = sys.argv[1] # add input XML file as second argument


# Edit file name here:
blast = NCBIXML.parse(open(inFile,'rU'))
#print(dir(blast))


# Get title for top hit one by one:
#blast_record = next(blast)
#print(dir(blast_record))
#print(blast_record.alignments[0])
#Repeat:
#blast_record = next(blast)
#print(blast_record.alignments[0])

# Above works. Wrap into a loop:
for blast_record in blast:
  if blast_record.alignments:
      print(blast_record.alignments[0].title)
      # Index takes top hit only
      print(blast_record.alignments[0].hsps[0].score)
        #print(dir(blast_record.alignments))
