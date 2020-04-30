import sys
import csv

def read_input(input_name, output_name, ref_name, dict_name):
	dict_file = open(dict_name, 'r')
	pos_dict = dict(csv.reader(dict_file, delimiter=';'))
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

		Asite_pos = get_codon_pos(input_list[9], int(input_list[3]), pos_dict)

		if Asite_pos != None:
			final_dict[seq_id][Asite_pos] += 1

	output_file = open(output_name, 'w')
	for entry in final_dict:
		try:
			output_file.write(entry)
			for counts in final_dict[entry]:
				output_file.write(';' + str(counts))
			output_file.write('\n')
		except:
			pass

def get_codon_pos(sequence, position, pos_dict):
	seq_len = str(len(sequence))
	if seq_len in pos_dict:
		if (position+int(pos_dict[seq_len]))%3==0 or pos_dict['miss']=='down' or (pos_dict['miss']=='round' and (position+int(pos_dict[seq_len]))%3==1):
			Asite_pos = int((position + int(pos_dict[seq_len]))/3)
			return Asite_pos
		elif pos_dict['miss']=='round' and (position+int(pos_dict[seq_len]))%3==2:
			Asite_pos = int((position + int(pos_dict[seq_len]))/3)+1
			return Asite_pos		
		else:
			return None
	else:
		return None

def main():
	if len(sys.argv)<5:
		print('use: SAM-CSV-builder.py <input> <output> <reference_fasta> <csv_with_values>')
		sys.exit()
	read_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


main()