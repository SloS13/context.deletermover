import xbmc
import xbmcaddon
import os
import xbmcgui
import xbmcplugin
import sys

def delete_file(file,title):
    
    
    
    if xbmcgui.Dialog().yesno( "Confirm Delete", "Confirm Delete For " + title + watchedFolderTvShows +"??", "", "", "Cancel", "Delete" ):
        if (currentPlayingFile==file):
            xbmc.executebuiltin('Notification(Item, ' + "Stopping video because it's playing" + ', 2)')
            xbmc.executebuiltin("PlayerControl(Stop)")
        if os.path.exists(file):
                os.remove(file)
                hbd = ' has been deleted'
                xbmc.executebuiltin("XBMC.CleanLibrary(video)")
                xbmc.executebuiltin('Notification(Item, ' + path + hbd + ', 2)')		
		
 
path = xbmc.getInfoLabel('ListItem.FileNameAndPath')
title = xbmc.getInfoLabel('ListItem.Title')

mytext = str(sys.argv[0])
xbmc.executebuiltin('Notification(Item, ' + mytext + ', 2)')

#watchedFolderMovies = xbmcaddon.getSetting("watchedFolderMovies")
watchedFolderTvShows = xbmcplugin.getSetting(int(sys.argv[1]), 'watchedFolderTvShows')

currentPlayingFile = xbmc.getInfoLabel("Player.Filenameandpath")
delete_file(path,title)





