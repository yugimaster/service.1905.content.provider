#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import traceback

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')


def log(txt):
    message = '%s: %s' % (ADDON_NAME, txt.encode('ascii', 'ignore'))
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)


def print_exc():
    traceback.print_exc()


def item_remap(detail):
    movieid = detail['id']
    art_dict = {"fanart": "",
                "landscape": "",
                "poster": detail['img']}
    casts = []
    for (count, k) in enumerate(detail['actor'].split(',')):
        item = {"name": k,
                "order": count,
                "role": "",
                "thumbnail": ""}
        casts.append(item)
    return {
        "art": art_dict,
        "cast": casts,
        "country": detail.get('clime').split(','),
        "dateadded": detail.get('fruntTime'),
        "director": detail.get('director').split(','),
        "file": "plugin://plugin.proxy.video?action=cctv_play&amp;cid={0}&amp;vid={1}".format(movieid, movieid),
        "path": "plugin://plugin.proxy.video?action=cctv_play&amp;cid={0}&amp;vid={1}".format(movieid, movieid),
        "genre": detail.get('mtypes'),
        "imdbnumber": "",
        "label": detail.get('title'),
        "lastplayed": "",
        "movieid": movieid,
        "mpaa": "",
        "originaltitle": detail.get('title'),
        "playcount": 0,
        "plot": detail.get('description'),
        "plotoutline": detail.get('description'),
        "rating": '0.0' if not detail.get('score') else str(detail.get('score')),
        "resume": {"position": 0, "total": detail.get('duration')},
        "runtime": detail.get('duration'),
        "streamdetails": {},
        "studio": [],
        "tagline": detail.get('title'),
        "title": detail.get('title'),
        "trailer": "",
        "votes": "",
        "writer": [],
        "year": str(detail.get('years'))
    }


def create_json_rpc(listitems, channel):
    json_query = {}
    json_query['id'] = 1
    json_query['jsonrpc'] = 2.0
    if listitems:
        json_query['result'] = {}
        json_query['result'][channel] = listitems
    return json_query
