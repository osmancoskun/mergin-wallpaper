import os
import json
import shutil
import requests
import subprocess
import gi
gi.require_version("GLib", "2.0")
gi.require_version("Gio", "2.0")
from gi.repository import GLib,Gio
class Utils():
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
    
    def send_notification(self,text):
        subprocess.run(['notify-send','Mergin', f'"{text}"'])

    def download_bing_wallpaper(self):
        jsonData = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
        wallpaperData = json.loads(jsonData.text)
        wallpaperLink = wallpaperData["images"][0]["url"][1:]
        wallpaperName = "BING-" + wallpaperData["images"][0]["startdate"] + ".jpg"
        wallpaperLink = wallpaperLink.split("&")[0]
        fullWallpaperLink = "https://www.bing.com/" + wallpaperLink
        
        #Downloading wallpaper
        subprocess.run(["wget" , fullWallpaperLink])
        shutil.move(wallpaperLink ,  "./src/"+wallpaperName)
        return wallpaperName
    
    def list_wallpapers():
        return os.listdir("./src")
    def set_wallpaper(self,wallpaper_name):
        path = f'file://{os.getcwd()}/src/{wallpaper_name}'

        mode_scheme = "org.gnome.desktop.interface"
        background_scheme = "org.gnome.desktop.background"
        
        mode_key = "color-scheme"
        background_key = "picture-uri"
        background_key_dark = "picture-uri-dark"

        mode_settings = Gio.Settings(mode_scheme)
        background_settings = Gio.Settings(background_scheme)

        scheme = mode_settings.get_string(mode_key)
        if "dark" in scheme:
            background_settings.set_string(background_key_dark,path)
        else:
            background_settings.set_string(background_key,path)

    def get_current_wallpaper():
        mode_scheme = "org.gnome.desktop.interface"
        background_scheme = "org.gnome.desktop.background"
        
        mode_key = "color-scheme"
        background_key = "picture-uri"
        background_key_dark = "picture-uri-dark"

        mode_settings = Gio.Settings(mode_scheme)
        background_settings = Gio.Settings(background_scheme)

        scheme = mode_settings.get_string(mode_key)
        if "dark" in scheme:
            return background_settings.get_string(background_key_dark)
        else:
            background_settings.get_string(background_key)


        