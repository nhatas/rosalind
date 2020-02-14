# problem 4

'''
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

import operator

dataset = open('rosalind.fa', 'r')
f = dataset.readlines()

gcDic = {}
gc_count = 0
at_count = 0
for line in f:
    if line.startswith('>'):
        header = line
        gc_count = 0
        at_count = 0
    else:
        for char in line:
            if char == 'G' or char == 'C':
                gc_count += 1
            if char == 'A' or char == 'T':
                at_count +=1
        gc_content = gc_count / (gc_count + at_count)
        gcDic.update( {header.rstrip() : gc_content} )
                
max_gc = max(gcDic.items(), key=operator.itemgetter(1))[0]
for key,value in gcDic.items():
    if key == max_gc:
        val = value
        
print(max_gc[1:])
print(val*100)

#print(gcDic)