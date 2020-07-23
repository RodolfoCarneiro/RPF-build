import sys
import csv

def read_input(input_name, output_name, ref_name):
	reference_file = open(ref_name, 'r')
	reference_data = str.split(reference_file.read(), '\n')
	final_dict = {}
	gene_len = 0
	gene_id = None
	for reference_code in reference_data:
		if reference_code != '':
			if reference_code[0] == '>':
				if reference_code[0] != None:
					final_dict[gene_id] = [0]*gene_len
				gene_id = str.split(reference_code, ' ')[0].replace('>', '')
				gene_len = 0
			else:
				gene_len += len(reference_code)
	final_dict[gene_id] = [0]*gene_len

	for input_entry in open(input_name, 'r'):
		input_list = str.split(input_entry, '\t')
		seq_id = input_list[2].replace('_W303', '')

		if not (seq_id in final_dict):
			continue

		sequence = input_list[9]
		seq_len = len(sequence)
		position = int(input_list[3])
		finalpos = position + seq_len + 1

		for currentpos in range(position, finalpos, 1):
			while len(final_dict[seq_id]) < finalpos:
				final_dict[seq_id].append(0)

			final_dict[seq_id][currentpos] += 1


	output_file = open(output_name, 'w')
	for entry in final_dict:
		if entry != None:
			output_file.write(str(entry))
			for counts in final_dict[entry]:
				output_file.write(';' + str(counts))
			output_file.write('\n')

def main():
	read_input(sys.argv[1], sys.argv[2], sys.argv[3])


main()