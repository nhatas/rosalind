#problem 1
'''
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

A_cnt = 0
G_cnt = 0
C_cnt = 0
T_cnt = 0

for char in string:
    if char == 'A':
        A_cnt += 1
    if char == 'G':
        G_cnt += 1
    if char == 'C':
        C_cnt += 1
    if char == 'T':
        T_cnt += 1
        
print(A_cnt, C_cnt, G_cnt, T_cnt)