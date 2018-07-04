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

import sys
import xbmcgui
import xbmcaddon
import xbmcplugin
from common import log
from resources.lib import data

ADDON = xbmcaddon.Addon()
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_LANGUAGE = ADDON.getLocalizedString


class Main:

    def __init__(self):
        self._init_vars()
        self._parse_argv()
        if not self.TYPE:
            return
        for content_type in self.TYPE.split("+"):
            full_liz = list()
            if content_type == "hotmovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('hotmovies', 31001, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
            if content_type == "vipmovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('vipmovies', 31002, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
            if content_type == "actionmovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('actionmovies', 31003, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
            if content_type == "comedymovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('comedymovies', 31004, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
            if content_type == "lovemovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('lovemovies', 31005, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
            if content_type == "cartoonmovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('cartoonmovies', 31006, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
            if content_type == "warmovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('warmovies', 31007, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
            if content_type == "classicmovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('classicmovies', 31008, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
            if content_type == "thrillermovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('thrillermovies', 31009, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
            if content_type == "minimovies":
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
                data.parse_movies('minimovies', 31010, full_liz, self.USECACHE, self.PLOT_ENABLE, self.LIMIT)
                xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]))

    def _init_vars(self):
        self.WINDOW = xbmcgui.Window(10000)
        self.SETTINGSLIMIT = int(ADDON.getSetting("limit"))
        self.PLOT_ENABLE = ADDON.getSetting("plot_enable") == 'true'

    def _parse_argv(self):
        try:
            params = dict(arg.split("=") for arg in sys.argv[2].split("&"))
        except Exception:
            params = {}
        self.TYPE = params.get("?type", "")
        self.ALBUM = params.get("album", "")
        self.USECACHE = params.get("reload", False)
        self.path = params.get("id", "")
        if self.USECACHE is not False:
            self.USECACHE = True
        self.LIMIT = int(params.get("limit", "-1"))
        self.dbid = params.get("dbid", "")
        self.dbtype = params.get("dbtype", False)


log('script version %s started' % ADDON_VERSION)
Main()
log('script version %s stopped' % ADDON_VERSION)
