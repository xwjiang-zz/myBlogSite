import boto
import time
import random

def post(userId, file, ext):
  s3 = boto.connect_s3('AKIAJYATR6L425DPRTWA','+3fh2iJz7Yfmr8A0P+q83e4Lm8X8q0cUEOkLN7lL')
  timeStamp = str(int(time.time())) 
  bucket = s3.get_bucket('ucsc_jessica')
  newKeyPath = 'images/' + str(userId) +'_' + timeStamp + '_' + str(random.randint(1, 100)) + ext
  newKey = bucket.new_key(newKeyPath)
  newKey.set_contents_from_file(file)
  newKey.set_acl('public-read')
  return newKeyPath 

def get(keyPath):
  s3 = boto.connect_s3('AKIAJYATR6L425DPRTWA','+3fh2iJz7Yfmr8A0P+q83e4Lm8X8q0cUEOkLN7lL')
  bucket = s3.get_bucket('ucsc_jessica')
  key = bucket.get_key(keyPath)
  return key.generate_url(86400*7)

