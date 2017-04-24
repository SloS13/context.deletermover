import xbmc
import xbmcaddon
import os
import xbmcgui
import xbmcplugin
import sys
import ntpath




def delete_file(file,title):
    
    
    
    if xbmcgui.Dialog().yesno( "Confirm " + action, "Confirm " + action + " For " + title  +"?", "", "", "Cancel", "Delete" ):
        if (currentPlayingFile==file):
            xbmc.executebuiltin('Notification(Item, ' + "Stopping video because it's playing" + ', 2)')
            xbmc.executebuiltin("PlayerControl(Stop)")
        if os.path.exists(file):
            filename = ntpath.basename(file)
            if ( action == 'Delete' ):
                os.remove(file)
                hbd = ' has been deleted'
            else:
                xbmc.log('SOURCE: ' + file, xbmc.LOGERROR)
                xbmc.log('TARGET: ' + watchedFolder  + filename, xbmc.LOGERROR)
                target = watchedFolder + '/' + filename
                #xbmc.executebuiltin('Notification(Item, ' + target + ', 2)')
                renameResult = os.rename(file, watchedFolder +  filename)
            xbmc.executebuiltin("XBMC.CleanLibrary(video)")
            xbmc.executebuiltin('Notification(Item, ' + title + hbd + ', 3)')		
		
 
path = xbmc.getInfoLabel('ListItem.FileNameAndPath')
title = xbmc.getInfoLabel('ListItem.Title')
__settings__ = xbmcaddon.Addon(id="context.deletermover")

if xbmc.getCondVisibility( 'VideoPlayer.Content(movies)' ):
    currentContent = 'movies'
    watchedFolder = __settings__.getSetting("watchedFolderMovies")
else:
    currentContent = 'tvshows'
    watchedFolder = __settings__.getSetting("watchedFolderTvShows")
    
    
watchedFolder = '' # Move wont work with Python so this is a delete-only thing (samba + windows problems...)
    
if (watchedFolder == ''):
    action = 'Delete'
else:
    action = 'Move'
    




currentPlayingFile = xbmc.getInfoLabel("Player.Filenameandpath")
delete_file(path,title)





