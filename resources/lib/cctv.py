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

import util


class CCTVClass():
    HOMEPOST = 'm.pt1905.gitv.tv'
    MENU_LIST_API = 'http://' + HOMEPOST + '/v22/film/'
    FILM_LIST_API = 'http://' + HOMEPOST + '/v22/film/album/'
    FILM_DETAIL_API = 'http://' + HOMEPOST + '/film/'
    TOKEN = "5dc652f5fa58449eb92febd2b198b2bf"
    MAC_ADDRESS = "d6:1c:54:42:4e:1b"

    def get_menu_list(self):
        url = self.MENU_LIST_API + 'menu?serverId={serverId}&channel_version={channel_version}&userId={userId}&mac={mac}&launcher_version={launcher_version}&token={token}&sn={sn}&client_id={client_id}&home_version={home_version}&from=filmlist'
        url = url.format(
            serverId=102,
            channel_version=102,
            userId=9130180,
            mac=self.MAC_ADDRESS,
            launcher_version="9000.1.05",
            token=self.TOKEN,
            sn="not_found",
            client_id=1080109,
            home_version=110)
        return util.GetHttpData(url)

    def get_movie_list(self, category, pagenum=1, pagesize=12):
        url = self.FILM_LIST_API + '{category}?page={pagenum}&size={pagesize}&serverId={serverId}&channel_version={channel_version}&userId={userId}&mac={mac}&launcher_version={launcher_version}&token={token}&sn={sn}&client_id={client_id}&home_version={home_version}&from=filmlist'
        url = url.format(
            category=category,
            pagenum=pagenum,
            pagesize=pagesize,
            serverId=102,
            channel_version=102,
            userId=9130180,
            mac=self.MAC_ADDRESS,
            launcher_version="9000.1.05",
            token=self.TOKEN,
            sn="not_found",
            client_id=1080109,
            home_version=110)
        return util.GetHttpData(url)

    def get_movie_detail(self, vid):
        url = self.FILM_DETAIL_API + '{vid}?serverId={serverId}&channel_version={channel_version}&userId={userId}&mac={mac}&launcher_version={launcher_version}&token={token}&sn={sn}&client_id={client_id}&home_version={home_version}'
        url = url.format(
            vid=vid,
            serverId=102,
            channel_version=102,
            userId=9130180,
            mac=self.MAC_ADDRESS,
            launcher_version="9000.1.05",
            token=self.TOKEN,
            sn="not_found",
            client_id=1080109,
            home_version=110)
        return util.GetHttpData(url)
