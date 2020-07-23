import sys
import csv

class Length:
	def __init__(self):
		self.count = [0]*100
		self.accepted = [0]*100
		log_name = sys.argv[2] + '_log.csv'
		self.log_file = open(log_name, 'w')

	def write(self):
		self.log_file.write('read length;total;accepted')
		output_text = ''
		for index in range(len(self.count)):
			output_text += '\n' + str(index) + ';' + str(self.count[index]) + ';' + str(self.accepted[index])
			if self.count[index] != 0 or self.accepted[index] != 0:
				self.log_file.write(output_text)
				output_text = ''


def read_input(input_name, output_name, ref_name, dict_name, nucleotides):
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
					final_dict[gene_id] = [0]*int(gene_len/nucleotides)
				gene_id = str.split(reference_code, ' ')[0].replace('>', '')
				gene_len = 0
			else:
				gene_len += len(reference_code)
	final_dict[gene_id] = [0]*gene_len

	length = Length()

	for input_entry in open(input_name, 'r'):
		input_list = str.split(input_entry, '\t')
		seq_id = input_list[2].replace('_W303', '')

		if not (seq_id in final_dict):
			continue

		Asite_pos = get_codon_pos(input_list[9], int(input_list[3]), pos_dict, length, nucleotides)

		if Asite_pos != None:
			final_dict[seq_id][Asite_pos] += 1

	length.write()
	output_file = open(output_name, 'w')

	for entry in final_dict:
		try:
			output_file.write(entry)
			for counts in final_dict[entry]:
				output_file.write(';' + str(counts))
			output_file.write('\n')
		except:
			pass

def get_codon_pos(sequence, position, pos_dict, length, nts):
	seq_len_int = len(sequence)
	length.count[seq_len_int] += 1

	seq_len = str(seq_len_int)
	if seq_len in pos_dict:
		length.accepted[seq_len_int] += 1
		if (position+int(pos_dict[seq_len]))%nts==0 or (position+int(pos_dict[seq_len]))%nts==1:
			Asite_pos = int((position + int(pos_dict[seq_len]))/nts)
			return Asite_pos
		elif (position+int(pos_dict[seq_len]))%nts==2:
			Asite_pos = int((position + int(pos_dict[seq_len]))/nts)+1
			return Asite_pos
	else:
		return None

def main():
	if len(sys.argv)<5:
		print('use: SAM-CSV-builder.py <input> <output> <reference_fasta> <csv_with_values>')
		sys.exit()

	nucleotides = 3
	if len(sys.argv)==6:
		if sys.argv[5] == 'nt':
			nucleotides = 1
	read_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], nucleotides)


main()