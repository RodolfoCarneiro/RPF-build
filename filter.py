import csv
import sys
if len(sys.argv)<4:
	print('use: <program_name> <input_file> <output_file> <min_reads_per_column>')
	sys.exit()

file1 = open(sys.argv[1], 'r')
read1 = list(csv.reader(file1, delimiter=';'))
output = open(sys.argv[2], 'w', newline='')
output_writter = csv.writer(output, delimiter=';')

final_output = []

for file1_line in read1:
	codon_count = 0.0
	codon_sum = 0.0
	for file1_codon in file1_line:
		try:
			codon_sum += float(file1_codon)
			codon_count += 1.0
		except:
			pass

	if codon_sum/codon_count >= int(sys.argv[3]):
		output_writter.writerow(file1_line)