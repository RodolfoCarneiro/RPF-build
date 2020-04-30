Takes a SAM file and converts it to a CSV list, in which the first column is the gene's identifier, and the following collumns are the number of reads on each codon of that gene.

Usage: SAM-CSV-builder.py <input_file.SAM> <output_file.CSV> <reference_genome.fa> <values_list.csv>

values_list.csv is a file that will be converted to a python dictionary, containing the A-site position relative to the length of the read.

References:
"Long" and "Short" values list follows the parameters from:
Matsuo,Y., Tesina,P., Nakajima,S. Mizuno,M., Endo,A., Buschauer,R., Cheng,J., Shounai,O., Ikeuchi,K., Saeki,Y., Becker,T. Beckmann,R., Inada,T. (2020) RQT complex dissociates ribosomes collided on endogenous RQC substrate SDD1. Nat. Struct. Mol. Biol., 4, 323-332.