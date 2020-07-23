import csv
import sys

if len(sys.argv) < 4:
	print('use: <program_name> <numerator_input> <denominator_input> <output_file>')
	sys.exit()

file1 = open(sys.argv[1], 'r')
read1 = list(csv.reader(file1, delimiter=';'))
file2 = open(sys.argv[2], 'r')
read2 = list(csv.reader(file2, delimiter=';'))
output = open(sys.argv[3], 'w')

for file1_line in read1:
	file1_gene = file1_line[0]

	file2_line = None
	for read2_line in read2:
		if read2_line[0] == file1_gene:
			file2_line = read2_line
			break

	if file2_line == None:
		continue

	maxlen = min([len(file1_line), len(file2_line)])
	for index2 in range(maxlen):

		if index2 == 0:
			output.write(file1_line[0])

		else:
			file1_codon = float(file1_line[index2])
			file2_codon = float(file2_line[index2])
			if file1_codon == 0.0:
				output.write(';')

			else:
				output_codon = str(file2_codon/file1_codon)
				output.write(';' + output_codon)

	output.write('\n')

