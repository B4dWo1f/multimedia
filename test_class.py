#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import IO


#def clean_name(string):
#   """
#     Removes underscores and extensions of files (last field after the
#     last dot). Naive title of the movie
#   """
#   if '.' in string or '_' in string:
#      string = string.split('.')[0:-1]
#      st = ''
#      for s in string:
#         st += s
#      name = st.replace('_',' ')
#   else: name = string
#   return name.title()


class my_peli():
   def __init__(self,rating=0.0,dur=0.0,year=0,languages=[],votes=0,
                title='',mpaa='',writer=[],certificates=[],
                country_codes=[],language_codes=[],cover_url='',
                genres=[],director=[],akas=[],aspect_ratio='',kind='',
                countries=[],plot_outline='',plot=[],cast=[],fil=''):
      self.rating = rating  # float
      #dur = []
      #try:
      #   for r in runtimes:
      #      try: dur.append(float(r))
      #      except: pass
      #except: dur = []
      #if len(dur) == 0: dur = 0.0
      self.duration = dur  # float
      #self.runtimes = np.mean([float(r) for r in runtimes])  # float
      self.year = year  # int
      #self.languages = languages  # list
      self.votes = votes  # int
      self.title = title  # unicode
      #self.mpaa = uni2ascii(mpaa)  # unicode
      #self.writer = writer  # list
      #self.certificates = certificates  # list
      #self.country_codes = country_codes  # list
      #self.language_codes = language_codes  # list
      self.cover_url = cover_url  # unicode
      self.genres = genres #[uni2ascii(g) for g in genres]  # list
      self.director = director #[D.data.get('name') for D in director]  # list
      #self.akas = akas  # list
      #self.aspect_ratio = uni2ascii(aspect_ratio)  # unicode
      self.kind = kind  # unicode
      #self.countries = countries  # list
      #self.plot_outline = uni2ascii(plot_outline)   # unicode
      #self.plot = plot  # list
      #self.cast = cast  # list
      self.fil = fil  # str
   def __str__(self):
      msg = self.title
      msg += ' (%s)\n'%(self.year)
      msg += '  Kind: %s\n'%(self.kind)
      msg += '  Rating: '+str(self.rating) + ' (%s)\n'%(self.votes)
      msg += '  Generos: '
      for g in self.genres:
         msg += g + ', '
      msg += '\n'
      msg += '  Sinopsis: '
      #msg += self.plot_outline + '\n'
      msg += self.cover_url + '\n'
      return msg
   def update(self,entries):
      self.__dict__.update(entries)
   def write(self):
      IO.json_write(self.__dict__,self.fil.split('.')[0]+'.json')
