#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import urllib2
import re

url = "http://www.blocket.se/stockholm?q=pentax"

response = urllib2.urlopen(url)
result = response.read()

print result

#m = re.findall('a id="tyda_transR\d+" href="/search/\w+',result)
#for s in m:
#    print s.split('"')[3].split('/')[2]
