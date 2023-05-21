import gi
import os
import json
import requests
import subprocess
gi.require_version("Gtk","4.0")
gi.require_version("Adw","1")
from gi.repository import Gtk,Adw,Gdk,Gio,GdkPixbuf
from Utils import Utils
from UI import UI

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self,*args,**kwargs):

        # Window initialization
        super().__init__(*args,**kwargs)
        self.window = Gtk.ApplicationWindow(title="Mergin Wallpaper")
        self.window.set_size_request(800,500)
        
        # CSS file
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('style.css')
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.popover = Gtk.PopoverMenu()  # Create a new popover menu
        self.ui_button_about = UI.Button.create(text="About")
        self.ui_button_about.connect('clicked',self.fun_show_about)
        self.popover.set_child(self.ui_button_about)
        
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic") 
        self.header = Gtk.HeaderBar()
        self.header.pack_start(self.hamburger)
        self.window.set_titlebar(self.header)

        self.ui_box_main = UI.Box.create(css=['mainbox'])


        self.ui_box_wallpaper = UI.Box.create(
            vexpand=True,
            orientation="vertical",
            css=['wallpaper-box']
        )
        
        self.init_wallpaper_list()        
        self.init_wallpaper_image()
        
        self.ui_box_wallpaper.append(self.ui_listbox_wallpapers)
        self.ui_box_main.append(self.ui_box_wallpaper)


        self.ui_box_content = UI.Box.create(orientation="vertical",hexpand=True)

        self.ui_box_buttons = UI.Box.create(
            hexpand=True,
            valign="start",
            spacing=13,
            margin_start=13,
            homogeneous=True,

        )
        self.ui_button_download = UI.Button.create(text="Download BING Wallpaper",hexpand=True)
        self.ui_button_download.connect('clicked',self.on_download_wallpaper)
        self.ui_button_set = UI.Button.create(text="Set Wallpaper",hexpand=True)
        self.ui_button_set.connect("clicked",self.on_set_wallpaper)

        self.ui_box_buttons.append(self.ui_button_download)
        self.ui_box_buttons.append(self.ui_button_set)
        self.ui_box_content.append(self.ui_box_buttons)
        self.ui_box_content.append(self.image)
        self.ui_box_main.append(self.ui_box_content)
        self.window.set_child(self.ui_box_main)


    def init_wallpaper_list(self):
        self.wallpaper_list = Utils.list_wallpapers()
        self.ui_listbox_wallpapers = Gtk.ListBox()
        self.ui_listbox_wallpapers.set_show_separators(True)
        self.ui_listbox_wallpapers.connect('row-activated',self.on_change_preview)
        self.ui_listbox_wallpapers.set_vexpand(True)

        for wallpaper in self.wallpaper_list:
            self.ui_listbox_wallpapers.append(self.fun_create_lbrow(wallpaper))
        
        self.ui_listbox_wallpapers.show()

    def init_wallpaper_image(self):
        self.current_wallpaper = self.wallpaper_list[0]
        self.image = Gtk.Image.new_from_file('./src/'+self.wallpaper_list[0])
        self.image.set_hexpand(True)
        self.image.set_vexpand(True)

    def on_change_preview(self,listbox,row):
        row_name = row.get_name()
        self.image.set_from_file(f"./src/{row_name}")
        self.current_wallpaper = row_name
        

    def on_set_wallpaper(self,button):
        Utils.set_wallpaper(self,wallpaper_name=self.current_wallpaper)

    def on_download_wallpaper(self,button):
        wallpaper_name = Utils.download_bing_wallpaper(self)
        self.ui_listbox_wallpapers.append(self.fun_create_lbrow(wallpaper_name))
        self.ui_listbox_wallpapers.show()
        Utils.send_notification(self,'Wallpaper downloaded')

    def fun_create_lbrow(self,text):
        lbr_wallpaper = UI.ListBoxRow.create(text=text)
        lbr_wallpaper.set_name(text)
        return lbr_wallpaper
    def fun_show_about(self,button):
        dialog=Adw.AboutWindow() 
        dialog.set_application_name=("Mergin Wallpaper") 
        dialog.set_version("1.0") 
        dialog.set_developer_name("Osman Coskun") 
        dialog.set_license_type(Gtk.License(Gtk.License.GPL_3_0)) 
        dialog.set_comments("Simple application for downloading BING wallpaper") 
        dialog.set_website("https://github.com/osmancoskun/mergin-wallpaper") 
        dialog.set_issue_url("https://github.com/osmancoskun/mergin-wallpaper/issues")
        dialog.add_credit_section("Contributors",['Osman Coskun']) 
        dialog.set_translator_credits("Osman Coskun") 
        dialog.set_copyright("© 2023 Humanity") 
        dialog.set_developers(["Osman Coskun"]) 
        dialog.set_application_icon("com.osmancoskun.mergin-wallpaper") # icon must be uploaded in ~/.local/share/icons or /usr/share/icons
        dialog.show()