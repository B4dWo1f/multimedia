#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata


def clean_name(string):
   """
     Removes underscores and extensions of files (last field after the
     last dot). Naive title of the movie
   """
   if '.' in string or '_' in string:
      #string = string.split('.')[0:-1]
      #st = ''
      #for s in string:
      #   st += s
      st = ''.join(string.split('.')[0:-1])
      name = st.replace('_',' ')
   else: name = string
   return name.title()


def uni2ascii(string,form='NFKD',cod='UTF-8',err='ignore'):
   """
     encode string into UTF-8
   """
   if isinstance(string,unicode):
      return unicodedata.normalize(form, string).encode(cod,err)
   else:
      return ''


if __name__ == '__main__':
   aaa = 'this_is_a_film.avi'
   print clean_name(aaa)
