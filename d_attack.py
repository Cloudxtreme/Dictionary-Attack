#!/usr/bin/python
from hashlib import md5
import sys

if len(sys.argv) != 3:
	print "Usage: %s <file of hashes> <word list>" % sys.argv[0]
	quit()

def bruteforce(hash_list, word_list):
	cracked_hashes = {}
	hashes = [line.strip() for line in open(hash_list, 'r')]

	for word in open(word_list, 'r'):
		word = word.rstrip()
		hash = md5(word).hexdigest()
		
		if hash in hashes:
			cracked_hashes[hash] = word
			hashes.remove(hash)
			if hashes == []:
				break
				
	return cracked_hashes			
	
cracked_hashes = bruteforce(sys.argv[1], sys.argv[2])
print cracked_hashes
