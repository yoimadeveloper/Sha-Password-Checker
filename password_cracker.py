import hashlib

file = open('top-10000-passwords.txt','r')
database_password = file.read()
file.close()


def crack_sha1_hash(hash):  
  for password in database_password.split('\n'):
    # print ('password = ',password)
    result_hash= hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if result_hash==hash:
      return password
  return "PASSWORD NOT IN DATABASE"