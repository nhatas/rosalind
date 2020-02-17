#problem 5
'''
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
'''

dataset = open('rosalind_hamm.txt', 'r')
f = dataset.readlines()
hamming = 0

for i,j in zip(f[0],f[1]):
    if i != j:
        hamming += 1
        
print(hamming)
