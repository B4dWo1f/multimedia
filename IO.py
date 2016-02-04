#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os


def decide(v):
   """
     Returns the proper form of a given value depending on its type
     For lists returns the string '[A,B,...]', for numbers just numbers...
   """
   if isinstance(v,list): return '['+','.join([decide(iv) for iv in v])+']'
   elif isinstance(v,str): return '\''+v+'\''
   elif isinstance(v,float) or isinstance(v,int): return str(v)
   elif v == None: return None
   else:
      print '---'
      print v
      print type(v)
      print '---'
      sys.exit('ERROR trying to convert value to string ---> dict')
      return v


def json_write(dic,fname='file.json',check=True):
   """
     Saves a dictionary into a json file. The final JSON file should contain a
     properly formatted python dictionary
   """
   json = '{'
   for k,v in zip(dic.keys(),dic.values()):
      entry = '\''+k+'\':'
      if decide(v) == None: continue
      entry += decide(v)
      json += entry + ', '
   json = json[:-2]+'}\n'
   with open(fname,'w') as f: f.write(json)
   if check:
      try: json_read(fname)
      except SyntaxError:
         os.system('cat %s'%(fname))
         os.system('rm %s'%(fname))
         sys.exit('ERROR: when saving JSON file (%s)'%(fname))



def json_read(fname):
   """
     Returns the dictionary contained in the JSON file
   """
   lines = open(fname,'r').readlines()
   if len(lines) == 1:
      return eval(lines[0].lstrip().rstrip())
   else:
      sys.exit('ERROR while reading JSON file (%s)'%(fname))

