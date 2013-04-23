#!/usr/bin/python
from hashlib import md5
import sys

if len(sys.argv) != 3:
	print "Usage: %s <file of hashes> <word list>" % sys.argv[0]
	quit()

	
def bruteforce(hashes, word, hash)
	hashes = [line.strip() for line in open(sys.argv[1], 'r')]
	print "Imported %d hashes" % len(hashes)

	for word in open(sys.argv[2], 'r'):
		word = word.rstrip()
		hash = md5(word).hexdigest()
		
		if hash in hashes:
			print "%s | %s" % (hash, word)
			hashes.remove(hash)
			if hashes == []:
				break

	print "%d hashes not cracked" % len(hashes)
	
	
bruteforce(sys.argv[1], sys.argv[2])
