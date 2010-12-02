#!/usr/bin/env python
# encoding: utf-8

import os
from os.path import join, getsize
#path = 'P:/trunk/pan'
#path = 'I:/oneview/dev/java/src'
#path = 'H:/'
#path = 'C:/jifeng/pj/fanyi'
path = 'C:/jifeng/pj/coolnote'
#fileSubfix = '.py'
fileSubfix = '.java'

totalLinesNr = 0
totalFileNr = 0
for root, dirs, files in os.walk(path):
   #print root, files
   if '.settings' in dirs:
                       dirs.remove('.settings')  # don't visit eclipse directories
   if '.svn' in dirs:
                       dirs.remove('.svn')  # don't visit svn directories
   for name in files:
        if name.endswith(fileSubfix):
            output = os.popen("wc -l '"+join(root,name) +"'").read().split()
            totalLinesNr = totalLinesNr + int(output[0])
            totalFileNr = totalFileNr + 1
            print output, totalLinesNr, totalFileNr

print 'Total lines:', totalLinesNr
print 'Total files processed:',totalFileNr