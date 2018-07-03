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
import xbmcaddon
from common import log


ADDON = xbmcaddon.Addon()
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON_NAME = ADDON.getAddonInfo('name')


class Main:
    def __init__(self):
        pass

    def _init_vars(self):
        self.Player = ""
        self.Monitor = Widgets_Monitor()

    def _daemon(self):
        # daemon is meant to keep script running at all time
        pass


class Widgets_Monitor(xbmc.Monitor):

    def __init__(self, *args, **kwargs):
        xbmc.Monitor.__init__(self)


class Widgets_Player(xbmc.Player):

    def __init__(self, *args, **kwargs):
        xbmc.Player.__init__(self)

    def onPlayBackStarted(self):
        pass

    def onPlayBackEnded(self):
        pass

    def onPlayBackStopped(self):
        pass


log('service version %s started' % ADDON_VERSION)
Main()
log('service version %s stopped' % ADDON_VERSION)
