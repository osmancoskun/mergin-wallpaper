import sys
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk,Adw
from MainWindow import MainWindow

class MerginWallpaper(Adw.Application):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs,application_id="com.osmancoskun.mergin-wallpaper")
        self.connect('activate',self.on_activate)
        self.window = None
        
    def on_activate(self,app):
        if not self.window:
            self.window = MainWindow().window
            self.window.set_application(self)
            self.window.present()

if __name__ == '__main__':
    MerginWallpaper().run(sys.argv)
