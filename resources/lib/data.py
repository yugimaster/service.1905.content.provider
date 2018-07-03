#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2018 PivosGroup
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import json
from resources.lib import library


ADDON = xbmcaddon.Addon()
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_LANGUAGE = ADDON.getLocalizedString
LIBRARY = library.LibraryFunctions()


def parse_movies(content_type, list_type, full_liz, useCache, plot_enable, limit, date_liz=None, date_type=None):
    json_query = _get_data(content_type, useCache)
    while json_query == "LOADING":
        xbmc.sleep(100)
        json_query = _get_data(content_type, useCache)

    count = 0
    if json_query:
        json_query = json.loads(json_query)
        if "result" in json_query and "movies" in json_query['result']:
            for movie in json_query['result']['movies']:
                if "cast" in movie:
                    cast = _get_cast(movie['cast'])

                # create a list item
                liz = xbmcgui.ListItem(movie['title'])
                liz.setInfo(type="Video", infoLabels={"Title": movie['title'],
                                                      "OriginalTitle": movie['originaltitle'],
                                                      "Year": movie['year'],
                                                      "Genre": _get_joined_items(movie.get('genre', "")),
                                                      "Studio": _get_first_item(movie.get('studio', "")),
                                                      "Country": _get_first_item(movie.get('country', "")),
                                                      "Plot": _get_plot(movie['plot'], plot_enable, movie['playcount']),
                                                      "PlotOutline": movie['plotoutline'],
                                                      "Tagline": movie['tagline'],
                                                      "Rating": str(float(movie['rating'])),
                                                      "Votes": movie['votes'],
                                                      "MPAA": movie['mpaa'],
                                                      "Director": _get_joined_items(movie.get('director', "")),
                                                      "Writer": _get_joined_items(movie.get('writer', "")),
                                                      "Cast": cast[0],
                                                      "CastAndRole": cast[1],
                                                      "mediatype": "movie",
                                                      "Trailer": movie['trailer'],
                                                      "Playcount": movie['playcount']})
                liz.setProperty("resumetime", str(movie['resume']['position']))
                liz.setProperty("totaltime", str(movie['resume']['total']))
                liz.setProperty("type", ADDON_LANGUAGE(list_type))
                liz.setProperty("dbid", str(movie['movieid']))
                liz.setProperty("imdbnumber", str(movie['imdbnumber']))
                liz.setProperty("fanart_image", movie['art'].get('fanart', ''))
                liz.setProperty("cid", str(movie['movieid']))
                liz.setArt(movie['art'])
                liz.setThumbnailImage(movie['art'].get('poster', ''))
                liz.setIconImage('DefaultVideoCover.png')
                liz.setPath(movie.get("path", ""))
                hasVideo = False
                for key, value in movie['streamdetails'].iteritems():
                    for stream in value:
                        if 'video' in key:
                            hasVideo = True
                        liz.addStreamInfo(key, stream)

                # if duration wasnt in the streaminfo try adding the scraped one
                if not hasVideo:
                    stream = {'duration': movie['runtime']}
                    liz.addStreamInfo("video", stream)
                full_liz.append((movie['file'], liz, False))

                if date_type is not None:
                    date_liz.append(movie[date_type])

                count += 1
                if count == limit:
                    break

        del json_query


def _get_cast(castData):
    listCast = []
    listCastAndRole = []
    for castmember in castData:
        listCast.append(castmember["name"])
        listCastAndRole.append((castmember["name"], castmember["role"]))
    return [listCast, listCastAndRole]


def _get_plot(plot, plot_enable, watched):
    if watched >= 1:
        watched = True
    else:
        watched = False
    if not plot_enable and not watched:
        plot = ADDON_LANGUAGE(32014)
    return plot


def _get_first_item(item):
    if len(item) > 0:
        item = item[0]
    else:
        item = ""
    return item


def _get_joined_items(item):
    if len(item) > 0:
        item = " / ".join(item)
    else:
        item = ""
    return item


def _get_data(content_type, useCache):
    return LIBRARY._fetch_movie_content(content_type, useCache=useCache)
