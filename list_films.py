#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from os import listdir
from os.path import isfile, join


def check_names(files):
   """
     Report incorrect names of files (spaces, brackets....)
   """
   review = []
   for f in files:
      peli = f.split('/')[-1]  # name of file
      if len(peli.split('.')) > 2: review.append(f)
      if "[" in peli: review.append(f)
      if "(" in peli: review.append(f)
      if "-" in peli: review.append(f)
      if ' ' in peli or '\[' in peli: review.append(f)
   if len(review) > 0:
      print 'Need reviewing'
      for r in review:
         print r
      exit()

if __name__ == '__main__':

   path = '/mnt/ARCADIA/Videos/peliculas'
   films = 'peliculas.txt'
   ignored = ['srt','nfo']

   onlyfiles = [ join(path,f) for f in listdir(path) if isfile(join(path,f)) ]

   files = []
   for f in onlyfiles:
      ext = f.split('.')[-1]
      if ext not in ignored: files.append(f)

   with open(films,'w') as f:
      for fi in files:
         f.write(fi+'\n')

