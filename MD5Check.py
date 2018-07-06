import hashlib
import os
import sys

_getfile = input("Filelocation: ")
orginal_key = input("Original key (if any): ")

with open(_getfile, 'rb') as fh:
    m5 = hashlib.md5()
    m_sha1 = hashlib.sha1()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m5.update(data)
        m_sha1.update(data)
    md5 = m5.hexdigest()
    sha1 = m_sha1.hexdigest()

print ('MD5: ', md5)
print ('SHA: ', sha1)

if str(orginal_key) == str(md5):
    print ("\033[1;32;40m *MD5: The key is authentic!")
else:
    print ("\033[1;31;40m MD5: The key is not authentic!")

if str(orginal_key) == str(sha1):
    print ("\033[1;32;40m *SHA1: The key is authentic!")
else:
    print ("\033[1;31;40m SHA1: The key is not authentic!")