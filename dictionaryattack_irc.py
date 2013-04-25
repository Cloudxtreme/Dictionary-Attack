# hashbruteforce.py
# (C) 2013 Martijn Gonlag
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 1, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from hashlib import md5
from urllib2 import urlopen
import sys 

class dictionaryattack:
    def __init__(self):
       self.allowed_functions = {'help': 1, 'crack': 10 }
		
    def echo(self, bot, sock, buffer):
        sock.msg(buffer.to, ' '.join(buffer.msg.split()[1:]))
		
    def help(self, bot, sock, buffer):
        sock.msg(buffer.to, "Usage: ")
        sock.msg(buffer.to, " * dictionaryattack.help")
        sock.msg(buffer.to, " * dictionaryattack.crack <hash list url> <word list url>")

    def crack(self, bot, sock, buffer):
        arguments = buffer.msg.split()
        cracked_hashes = {}
        hashes = [line.strip() for line in urlopen(arguments[1])]
		
        for word in urlopen(arguments[2]):
            word = word.rstrip()
            hash = md5(word).hexdigest()

            if hash in hashes:
                cracked_hashes[hash] = word
                hashes.remove(hash)

            if hashes == []:
                break

        for hash in cracked_hashes:
            if hash: sock.msg(buffer.to, "Found %s as %s" % (hash, cracked_hashes[hash]))
