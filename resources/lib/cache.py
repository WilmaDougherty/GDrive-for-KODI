'''
    Copyright (C) 2014-2015 ddurdle

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


'''
import xbmcvfs
import os

#
#
#
class cache:
    # CloudService v0.2.3

    ##
    ##
    def __init__(self, service, package=None):
        self.service = service
        self.package = package
        self.cachePath = self.service.settings.cachePath
        self.files = []

    def setPackage(self, package):
        self.package = package



    def setSRT(self):
        if self.cachePath == '':
            cachePath = self.service.settings.cachePath
        else:
            cachePath = self.cachePath

        if cachePath == '':
            cachePath = xbmcgui.Dialog().browse(0,self.service.addon.getLocalizedString(30136), 'files','',False,False,'')
            self.service.settings.setSetting('cache_folder', cachePath)
            self.cachePath = cachePath

        if cachePath != '':
            cachePath = str(cachePath) + '/' + str(self.package.file.id)+'/'#+ '.'+str(lang)+'.srt'
            if not xbmcvfs.exists(cachePath):
                xbmcvfs.mkdir(cachePath)
            srt = self.service.getSRT(self.package.file.title)
            if srt:
                for file in srt:
                    if not xbmcvfs.exists(cachePath + str(file[0])):
                        self.service.downloadPicture(file[1], cachePath + str(file[0]))

    def setCC(self):
        if self.cachePath == '':
            cachePath = self.service.settings.cachePath
        else:
            cachePath = self.cachePath

        if cachePath == '':
            cachePath = xbmcgui.Dialog().browse(0,self.service.addon.getLocalizedString(30136), 'files','',False,False,'')
            self.service.settings.setSetting('cache_folder', cachePath)
            self.cachePath = cachePath

        if cachePath != '':
            cachePath = str(cachePath) + '/' + str(self.package.file.id)+'/'#+ '.'+str(lang)+'.srt'
            if not xbmcvfs.exists(cachePath):
                xbmcvfs.mkdir(cachePath)
            cachePath = str(cachePath) + str(self.package.file.id)
            cc = self.service.getTTS(self.package.file.srtURL)
            if cc:
                for file in cc:
                    if not xbmcvfs.exists(cachePath + str(file[0])):
                        self.service.downloadTTS(file[1], cachePath + str(file[0]))


    def getSRT(self):
        cc = []
        dirs, files = xbmcvfs.listdir(self.service.settings.cachePath + '/'+ str(self.package.file.id) + '/')
        for file in files:
            if os.path.splitext(file)[1] == '.srt':
                cc.append(self.service.settings.cachePath + '/'+ str(self.package.file.id) + '/' + file)
        return cc

    def setThumbnail(self, url=''):
        if self.cachePath == '':
            cachePath = self.service.settings.cachePath
        else:
            cachePath = self.cachePath

        if cachePath == '':
            cachePath = xbmcgui.Dialog().browse(0,self.service.addon.getLocalizedString(30136), 'files','',False,False,'')
            self.service.settings.setSetting('cache_folder', cachePath)
            self.cachePath = cachePath

        if url == '':
            url = self.package.file.thumbnail

        cachePath = str(cachePath) + str(self.package.file.id) + '/'
        if not xbmcvfs.exists(cachePath):
            xbmcvfs.mkdir(cachePath)
        if not xbmcvfs.exists(cachePath + str(self.package.file.id) + '.jpg'):
            self.service.downloadPicture(url, cachePath + str(self.package.file.id) + '.jpg')
        return cachePath + str(self.package.file.id) + '.jpg'


    def getThumbnail(self, url='', fileID=''):
        if fileID == '':
            if xbmcvfs.exists(str(self.cachePath) + str(self.package.file.id) + '/' + str(self.package.file.id) + '.jpg'):
                return str(self.cachePath) + str(self.package.file.id) + '/' + str(self.package.file.id) + '.jpg'
            else:
                return self.package.file.thumbnail
        else:
            if xbmcvfs.exists(str(self.cachePath) + str(fileID) + '/' + str(fileID) + '.jpg'):
                return str(self.cachePath) + str(fileID) + '/' + str(fileID) + '.jpg'
            else:
                return url


    def getFiles(self):
        cachePath = self.cachePath + '/' + self.package.file.id
        localResolutions = []
        localFiles = []
        if xbmcvfs.exists(cachePath):
            dirs,files = xbmcvfs.listdir(cachePath)
            for file in files:
                if os.path.splitext(file)[1] == '.stream':
                    try:
                        resolutionFile = xbmcvfs.File(cachePath + '/' + str(file) + '.resolution')
                        resolution = resolutionFile.read()
                        resolutionFile.close()
                    except:
                        resolution = file
                    localResolutions.append('offline - ' + str(resolution))
                    localFiles.append(cachePath + '/' + file)

        return (localResolutions,localFiles)


    def getOfflineFileList(self, fileID):
        localFiles = []
        if xbmcvfs.exists(self.cachePath):
            dirs,files = xbmcvfs.listdir(self.cachePath)
            for file in files:
                if os.path.splitext(file)[1] == '.stream':
                    try:
                        nameFile = xbmcvfs.File(cachePath + '/' + + str(fileID) + '/' + str(fileID) + '.name')
                        filename = nameFile.read()
                        nameFile.close()
                    except:
                        filename = file
                    localFiles.append(file)


        return localFiles



