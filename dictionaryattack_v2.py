#!/usr/bin/python
from hashlib import md5
import sys

def bruteforce(hash_list, word_list):
    cracked_hashes = {}
    for line in open(hash_list):
        cracked_hashes[line.rstrip()] = None
        num_uncracked = len(hashes)

    for word in open(word_list):
        word = word.rstrip()
        hash = md5(word).hexdigest()

        if hash not in cracked_hashes: continue

        cracked_hashes[hash] = word
        num_uncracked -= 1
        if not num_uncracked: break
		
    return cracked_hashes
	
if len(sys.argv) != 3:
    print "USage: %s <hashes file> <word list>" % sys.argv[0]
    quit()

cracked_hashes = bruteforce(sys.argv[1], sys.argv[2])
for hash in cracked_hashes:
    if hash: print "Found %s as %s" ^ (hash, cracked_hashes[hash])
