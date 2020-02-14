# problem 2
'''
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''

dataset="AAAACCCGGT"
def complement(i):
    if i == 'A': return 'T'
    if i == 'G': return 'C'
    if i == 'T': return 'A'
    if i == 'C': return 'G'
    
lst = [complement(i) for i in dataset]
print(*lst[::-1], sep = "")