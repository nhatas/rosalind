# problem 3

'''
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''

dataset="GATGGAACTTGACTACGTAAATT"
def complement(i):
    if i == 'A': return 'A'
    if i == 'G': return 'G'
    if i == 'T': return 'U'
    if i == 'C': return 'C'
    
lst = [complement(i) for i in dataset]
print(*lst, sep = "")