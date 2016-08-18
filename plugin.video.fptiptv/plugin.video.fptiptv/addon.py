#!/usr/bin/env python
# coding: utf-8

from xbmcswift2 import Plugin
import urlfetch
from BeautifulSoup import BeautifulSoup
import xbmcaddon
import xbmcgui
import xbmc
import json
import re
import urllib

plugin = Plugin()

crawurl = 'https://fptplay.net/'

result = urlfetch.fetch(
        "https://fptplay.net/user/login",
		data={"phone": "84969193281",
            "password": "911911",
            "submit":""
            },
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
			'Referer':'https://fptplay.net/'
            })
cookie2='laravel_session=' + result.cookies.get('laravel_session') + ";"



	
def getLinkById(id = None, quality = "2",cookie =None):

    #plugin.log.info(csrf)
    result = urlfetch.post(
        'https://fptplay.net/show/getlinklivetv',
        data={"id": id,
            "quality": quality,
            "mobile": "web",
			"type" : "newchannel"
            },
        headers={'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest',
                'Referer':'https://fptplay.net/livetv',
                'cookie':cookie
                }
        )
    
    if result.status_code != 200 :
        return None
    info = json.loads(result.content)
    return info['stream']





xbmc.executebuiltin('StopPVRManager')
xbmc.executebuiltin("ActivateWindow(10000)")

pDialog = xbmcgui.DialogProgress()
pDialog.create('[COLOR yellow]Lấy danh sách tv[/COLOR]','[COLOR red][B] Đang tải...[/B][/COLOR]')
xbmc.sleep(1000)

__setting= xbmcaddon.Addon(id='plugin.video.fptiptv')
fl=__setting.getSetting('file')	

dophangiai=__setting.getSetting('quality')
dpg=["chunklist_b300000","chunklist_b500000","chunklist_b1200000","chunklist_b2500000"]
d=int(dophangiai)

	
foo =open(fl,'w')
foo.write("#EXTM3U\n")

ten=['Cần thơ','Vĩnh Long 1','Vĩnh Long 2','Đồng Tháp','VTV1','VTV2','VTV3','VTV6','VTC1','VTC2','VTC3','VTC4','VTC9 LETS VIET','VTC14-Tin tức','HTV2','HTV3','HTV4','HTV7','Tiền Giang','An giang','Hậu Giang','Phim','[COLOR yellow]Kênh Phim[/COLOR]','[COLOR yellow]Thể thao tv[/COLOR]','[COLOR yellow]Bóng đá tv[/COLOR]']
dd=['can-tho','thvl1','vinh-long-2','dong-thap','vtv1-hd','vtv2',"vtv3-hd","vtv6-hd",'vtc1','vtc2','vtc3-hd','yeah1-family-vtc4','lets-viet','vtc14-hd','htv2','htv3','htv4','htv7-hd','tien-giang','an-giang','hau-giang','imovie-hd','kenh-phim','the-thao-tv','bong-da-tv',]

for x in range (0,25):
	
	temp=getLinkById(dd[x],2,cookie2)
	foo.write("#EXTINF:-1,"+ten[x]+'\n')
	foo.write(temp.replace("playlist",dpg[d],1)+'\n')
	pDialog.update(x*4,"[COLOR red][B] Đang thêm [/B][/COLOR]"+ten[x])
		
foo.close()
pDialog.close()

xbmc.executebuiltin('StartPVRManager')
xbmc.executebuiltin("ActivateWindow(10615)")


 