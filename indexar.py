#!/usr/bin/env python
# -*- coding: UTF-8 -*-

##import sys
#import os
#HOME = os.environ['HOME']
#here = os.path.dirname(os.path.abspath(__file__))
###sys.path.insert(0, '%s/JARVIS/pylibs'%(HOME))
##from clases import clean_name, save_list
#from time import sleep
##import pp

import numpy as np
import os
from random import randint
import imdb
import unicodedata
from test_class import my_peli
from strings import clean_name,uni2ascii
import IO


jar_path = '/var/jarvis'
jar_path = '.'


#def uni2ascii(string,form='NFKD',cod='UTF-8',err='ignore'):
#   if isinstance(string,unicode):
#      return unicodedata.normalize(form, string).encode(cod,err)
#   else:
#      return ''


def get_film(data,fil=''):
   try: title = uni2ascii(data.get('title')).replace('\'','')
   except: title = ''
   try: year = int(data.get('year'))
   except: year = 0
   rate = data.get('rating')
   votes = data.get('votes')
   ## Duration
   runtimes = data.get('runtimes')
   dur = []
   try:
      for r in runtimes:
         try: dur.append(float(r))
         except: pass
   except: dur = []
   if len(dur) == 0: dur = 0.0
   dur = np.mean(dur)
   ## Languages
   languages = data.get('languages')
   mpaa = data.get('mpaa')
   writer = data.get('writer')
   certs = data.get('certificates')
   co_codes = data.get('country codes')
   lan_codes = data.get('language codes')
   cover_url = uni2ascii(data.get('cover url'))
   ## Genres
   try: gen = [uni2ascii(g) for g in data.get('genres')]
   except: gen = ['']
   ## Director
   try: director =[uni2ascii(D.data.get('name')) for D in data.get('director')]
   except: director = ['']
   akas = data.get('akas')
   asp_rat = data.get('aspect ratio')
   ## Kind
   try: kind = uni2ascii(data.get('kind'))
   except: kind = ''
   country = data.get('countries')
   outline = data.get('plot outline')
   plot = data.get('plot')
   cast = data.get('cast')

   peli = my_peli(rating=rate,dur=dur,year=year,languages=languages,
                  votes=votes,title=title,mpaa=mpaa,writer=writer,
                  certificates=certs,country_codes=co_codes,
                  language_codes=lan_codes,cover_url=cover_url,genres=gen,
                  director=director,akas=akas,aspect_ratio=asp_rat,
                  kind=kind,countries=country,plot_outline=outline,plot=plot,
                  cast=cast,fil=fil)
   return peli


if __name__ == '__main__':
   pelis = open('peliculas.txt').readlines()
   folder = 'films'
   #fname = '%s/failed.log'%(jar_path)
   #os.system('rm %s'%(fname))

   names = []
   for p in pelis:
      names.append(clean_name(p.rstrip()))


   i = randint(0,300)
   i=212
   peliculas = []
   for i in range(len(names)):
      p = names[i]
      fname = pelis[i].lstrip().rstrip().split('.')[0]+'.json'
      fname = folder+'/'+fname

      if not os.path.isfile(fname):
         print 'Doing',fname
         ia = imdb.IMDb()

         s_result = ia.search_movie(p)
         if len(s_result) > 0:
            first_result = s_result[0]
            ia.update(first_result)
            data = first_result.data
            P = get_film(data,pelis[i].lstrip().rstrip())
            peliculas.append(P)
            IO.json_write(P.__dict__,fname)
         else:
            print '  Error:',p
      else: pass #print 'Skipping:', fname
      if os.path.isfile('STOP'): exit()
