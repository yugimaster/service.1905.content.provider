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
import json
from cctv import CCTVClass
from cache import CacheFunc
from common import *
from time import gmtime, strftime


PLOT_ENABLE = True


class LibraryFunctions():

    def __init__(self):
        self.WINDOW = xbmcgui.Window(10000)
        self.CCTV = CCTVClass()
        self.CACHE = CacheFunc()

    def _get_data_from_property(self, content_type, useCache):
        # Check if data is being refreshed elsewhere
        if self.WINDOW.getProperty(content_type + "-data") == "LOADING":
            for count in range(30):
                xbmc.sleep(100)
                data = self.WINDOW.getProperty(content_type + "-data")
                if data != "LOADING":
                    return data

        if useCache:
            # Check whether there is saved data
            if self.WINDOW.getProperty(content_type + "-data") is not "":
                return self.WINDOW.getProperty(content_type + "-data")

            # We haven't got any data, so don't send back anything
            return None

    # Common infrastructure for all queries: Use the cache if specified,
    # set the property to "LOADING" while the query runs,
    # set the timestamp and property correctly
    def _fetch_items(self, useCache=False, prefix=None, queryFunc=None):
        data = self._get_data_from_property(prefix, useCache)
        if data is not None:
            return data
        self.WINDOW.setProperty(prefix + "-data", "LOADING")

        rv = queryFunc()   # Must return a unicode string (json-encoded data)

        self.WINDOW.setProperty(prefix + "-data", rv)
        self.WINDOW.setProperty(prefix, strftime("%Y%m%d%H%M%S", gmtime()))
        return rv

    def json_query_movie_category(self, category, pagenum, pagesize, limit=20):
        result = self._fetch_movie_list(category, pagenum, pagesize)
        listitems = []
        count = 0
        if result is None:
            return None
        if "filmList" in result:
            for item in result['filmList']:
                detail_data = self._fetch_movie_detail(item['id'])
                if not detail_data:
                    continue
                listitem = item_remap(detail_data['film'])
                listitems.append(listitem)
                count += 1
                if count == limit - 1:
                    break
        json_query = create_json_rpc(listitems, "movies")
        rv = json.dumps(json_query)
        return unicode(rv, 'utf-8', errors='ignore')

    # Movies in different category
    def _fetch_movie_content(self, content_type, pagenum=1, pagesize=12, useCache=False):
        if content_type == "hotmovies":
            categoryId = 9000001
            category = "hot"

        def query_movie_category():
            return self.json_query_movie_category(categoryId, pagenum, pagesize)
        return self._fetch_items(useCache, category + "movies", query_movie_category)

    def _fetch_category_list(self, useCache=True):
        if useCache:
            data = self.CACHE.get_cache("category_list", "cctv")
            try:
                if data:
                    return data
            except Exception:
                log("old format cache")
        data = self.CCTV.get_menu_list()
        data = json.loads(data)
        result = None
        if data and data.get('code') == 2000 and "data" in data:
            self.CACHE.set_cache("category_list", data['data'], "cctv", 0)
            result = data['data']
        return result

    def _fetch_movie_list(self, category, pagenum, pagesize, useCache=True):
        if useCache:
            data = self.CACHE.get_cache("movie_list", "cctv_" + str(category) + "_" + str(pagenum))
            try:
                if data:
                    return data
            except Exception:
                log("old format cache")
        data = self.CCTV.get_movie_list(category, pagenum, pagesize)
        data = json.loads(data)
        result = None
        if data and data.get('code') == 2000 and "data" in data:
            self.CACHE.set_cache("movie_list", data['data'], "cctv_" + str(category) + "_" + str(pagenum), 0)
            result = data['data']
        return result

    def _fetch_movie_detail(self, vid, useCache=True):
        if useCache:
            data = self.CACHE.get_cache("movie_detail", "cctv_" + str(vid))
            try:
                if data:
                    return data
            except Exception:
                log("log format cache")
        data = self.CCTV.get_movie_detail(vid)
        data = json.loads(data)
        result = None
        if data and data.get('code') == 2000 and "data" in data:
            self.CACHE.set_cache("movie_detail", data['data'], "cctv_" + str(vid), 0)
            result = data['data']
        return result
