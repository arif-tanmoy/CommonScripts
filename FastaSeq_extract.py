#!/usr/bin/env python
'''
©Arif Mohammad Tanmoy (arif.tanmoy@gmail.com)
Use: python FastaSeq_extract.py --fasta <FASTA_File> --query <QUERY_ID_File> --out <OUTPUT_Fasta_File>
python packages: Biopython (tested with version 1.72), argparse.
'''
from Bio import SeqIO
from argparse import (ArgumentParser, FileType)

def parse_args():
	"Parse the input arguments, use '-h' for help"
	commands = ArgumentParser(description='Extract query sequence from FASTA file.')
	commands.add_argument('--fasta', type=str, required=True, help='Fasta Sequence file (Required).')
	commands.add_argument('--query', type=str, required=True, help='query ID file (Required)')
	commands.add_argument('--out', type=str, required=False, help='Output file with query sequence.', default='Output.fasta')
	return commands.parse_args()
args = parse_args()

# Let's define a finding tool
def find_id(idlist, qid):
	for i in range(0, len(idlist)):
		if qid in idlist[i]:
			return i
	return 'Not Found'

idd = []
seq = []
for rec in SeqIO.parse(open(args.fasta,"r"), 'fasta'):
	idd.append(str(rec.id))
	seq.append(str(rec.seq))

query = []
for line in open(args.query,"r"):
	query.append(line.rstrip())

output = open(args.out,"w")
for i in range(0, len(query)):
	j = find_id(idd, str(query[i]))
	if j != 'Not Found':
		print 'Found: '+str(query[i])
		result = ">" + str(idd[j]) + '\n' + str(seq[j])+ '\n'
		output.write(result)


'''
for i in range(0, len(query)):
	j = idd.find(str(query[i]))
	if j == -1:
		pass
	else:
		print str(query[i])
		k = idd.index(str(query[i]))
		result = ">" + str(idd[k]) + '\n' + str(seq[k])+ '\n'
		output.write(result)
'''
