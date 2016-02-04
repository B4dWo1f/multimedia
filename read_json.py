#!/usr/bin/env python
# -*- coding: UTF-8 -*-

lines = open('films/2001_odisea_en_el_espacio.json','r').readlines()
if len(lines) == 1:
   A = eval(lines[0].lstrip().rstrip())
else:
   print 'ERROR in JSON file'
   exit()
print A
print type(A)




from test_class import my_peli
s = my_peli()
s.update(A)
print 
print s



#import json
#d = json.loads(lines[0].lstrip().rstrip())
#A = {'rating':7.2, 'votes':38306, 'title':'Los cronocrímenes', 'genres':['Horror','Sci-Fi','Thriller'], 'cover_url':'http://ia.media-imdb.com/images/M/MV5BMTk3MzMyMTY4N15BMl5BanBnXkFtZTcwODI3OTUwMg@@._V1._SX97_SY140_.jpg', 'runtimes':92.0, 'director':['Vigalondo, Nacho'], 'year':2007, 'kind':'movie', 'fil':'cronocrimenes.avi'}

