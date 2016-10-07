#!/usr/bin/env python
# coding: utf-8

from xbmcswift2 import Plugin
import urlfetch

import xbmcaddon
import xbmcgui
import xbmc
import json
import re
import urllib
import base64
cns=[]
plugin = Plugin()

def getAllChannels():
    cns = []
    cns.extend(getChannels(""))
    return cns


@plugin.route('/')
def index():
    cns = getAllChannels()
    return cns

    
	

def getChannels(url): 
	cn=[]
	request=urlfetch.get("http://textuploader.com/5nxwo/raw")
	print request.content
	lines = request.content.splitlines()
	i = 0
	imgthumbnail="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSnHQRu0ZFx59gCy8NFjszGCW3RvF9MlkoH-249bakacrH22Eod"
	while i < len(lines):
			title=lines[i]
			channelid=lines[i+1]
			i+= 2
			cn = {
                'label': title,
                'path': channelid,
                'thumbnail':imgthumbnail,
                'is_playable': True
				}
			cns.append(cn)
  
	return cns

if __name__ == '__main__':
    plugin.run()
