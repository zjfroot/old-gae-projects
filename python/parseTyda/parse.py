#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import urllib2
import re

url = "http://tyda.se/search/tystl%C3%A5ten"

response = urllib2.urlopen(url)
result = response.read()

m = re.findall('a id="tyda_transR\d" href="/search/\w+',result)
for s in m:
    print s.split('"')[3].split('/')[2]