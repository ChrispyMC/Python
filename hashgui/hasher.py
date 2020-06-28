import os, io, hashlib

def test():
  print("Test!")

BUFFER_SIZE = 1024

def get_function(function="SHA3-256"):
  return {
    "BLAKE2B": hashlib.blake2b(),
    "BLAKE2S": hashlib.blake2s(),
    "MD5": hashlib.md5(),
    "SHA1": hashlib.sha1(),
    "SHA-224": hashlib.sha224(),
    "SHA-256": hashlib.sha256(),
    "SHA-384": hashlib.sha384(),
    "SHA-512": hashlib.sha512(),
    "SHA3-224": hashlib.sha3_224(),
    "SHA3-256": hashlib.sha3_256(),
    "SHA3-384": hashlib.sha3_384(),
    "SHA3-512": hashlib.sha3_512(),
    "SHAKE-128": hashlib.shake_128(),
    "SHAKE-256": hashlib.shake_128()
  }.get(function.upper(), None)

def hash_file(filename=None, function="SHA3-256"):
  if filename is None:
    print("No filename was given.")
    return False
  elif not os.path.isfile(filename):
    print(filename + " is not a file.")
    return False

  if get_function(function) is None:
    print("Invalid function name: " + function)
    return False
  else:
    hasher = get_function(function)

  with open(filename, "rb") as f:
    data = f.read(BUFFER_SIZE)
    while data:
      data = f.read(BUFFER_SIZE)
      hasher.update(data)
  return hasher.hexdigest()

"""
def hash_directory(directory=None, function="SHA3-256"):
  if directory is None:
    print("No directory was given.")
    return False
  elif not os.path.isdir(directory):
    print(directory + " is not a directory.")
    return False
  
  if get_function(function) is None:
    print("Invalid function name: " + function)
    return False
  else:
    hasher = get_function(function)
  
  #for file in directory
"""
