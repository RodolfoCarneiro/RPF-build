Takes a SAM file and converts it to a CSV list, in which the first column is the gene's identifier, and the following collumns are the number of reads on each codon of that gene. Each output column represents a codon. Use "nt" on the end of the command line to write the output in nucleotides instead of codons.

Usage: SAM-CSV-builder.py <input_file.SAM> <output_file.CSV> <reference_genome.fa> <values_list.csv>

values_list.csv is a file that will be converted to a python dictionary, containing the A-site position relative to the length of the read.

OTHER ALGORITHMS

SAM-CSV-builder-simple.py
Does not predict the A-site for the ribosome, counting every nucleotide in the read. Each output column represents a nucleotide.
Usage: SAM-CSV-builder.py <input_file.SAM> <output_file.CSV> <reference_genome.fa>

filter.py
Discards every gene that does not have a certain amount of reads per codon. The input file here is a CSV file, preferably the output from the previous programs.
Usage: filter.py <input_file> <output_file> <reads_threshold>

proportion.py
Uses two CSV inputs and creates a third CSV file that corresponds to the proportion of reads between the two inputs. The input files here are CSV files, preferably outputs from the previous programs.
Usage: proportion.py <numerator_input> <denominator_input> <output_file>


References:
"Long" and "Short" values list follows the parameters from:
Matsuo,Y., Tesina,P., Nakajima,S. Mizuno,M., Endo,A., Buschauer,R., Cheng,J., Shounai,O., Ikeuchi,K., Saeki,Y., Becker,T. Beckmann,R., Inada,T. (2020) RQT complex dissociates ribosomes collided on endogenous RQC substrate SDD1. Nat. Struct. Mol. Biol., 4, 323-332.