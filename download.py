#!/usr/bin/env python2.7

import os
import shutil
import time
import urllib2

baseurl = 'http://live-promotions.apple.com/drop/'
m3u8url = baseurl + 'champaign_640_.m3u8'
directory = "files/"

if not os.path.exists(directory):
  os.makedirs(directory)

downloaded = set()
while True:
  for line in urllib2.urlopen(m3u8url):
    if line.strip().endswith(".ts"):
      filename = line.strip()
      if filename not in downloaded:
        print "Downloading " + filename
        response = urllib2.urlopen(baseurl + filename)
        with open(directory + filename, 'wb') as fp:
          shutil.copyfileobj(response, fp)
        downloaded.add(filename)
  time.sleep(2)
