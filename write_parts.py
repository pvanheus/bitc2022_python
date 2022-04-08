# the three parameters of my algorithm
my_dna = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
cut_offset = 1
motif = 'GAATTC'

# the algorithm itself
# how long are my DNA fragments?
string_length = len(my_dna)
match_pos = my_dna.find(motif)
cut_position = match_pos + cut_offset
part1 = my_dna[0:cut_position]
part2 = my_dna[cut_position:]

output_file = open("mydna.txt", "w")
output_file.write(part1 + "\n")
output_file.write(part2 + "\n")
output_file.close()
