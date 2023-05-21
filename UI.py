import gi
gi.require_version("Gtk","4.0")
gi.require_version("Adw","1")
from gi.repository import Gtk,Adw


settings={
      'fill':Gtk.Align(0),
      'start':Gtk.Align(1),
      'end':Gtk.Align(2),
      'center':Gtk.Align(3),
      'baseline':Gtk.Align(4),
      'horizontal':Gtk.Orientation(0),
      'vertical':Gtk.Orientation(1)
}


class UI():
    class Box(Gtk.Box):
        def create(orientation="horizontal",
                    homogeneous=False,
                    spacing=0,
                    height=-1,
                    width=-1,
                    css=[],
                    hexpand=False,
                    vexpand=False,
                    halign="fill",
                    valign="fill",
                    margin_bottom=-1,
                    margin_top=-1,
                    margin_start=-1,
                    margin_end=-1,
                    
                    ):
            box = Gtk.Box.new(settings[orientation],spacing)
            box.set_homogeneous(homogeneous)
            box.set_size_request(width,height)
            box.set_css_classes(css)
            box.set_hexpand(hexpand)
            box.set_vexpand(vexpand)
            box.set_halign(settings[halign])
            box.set_valign(settings[valign])
            box.set_margin_bottom(margin_bottom)
            box.set_margin_top(margin_top)
            box.set_margin_start(margin_start)
            box.set_margin_end(margin_end)
            
            
            return box
    class ListBoxRow(Gtk.ListBoxRow):
        def create(text=""):
            listboxrow = Gtk.ListBoxRow()
            label = Gtk.Label(label=text)
            listboxrow.set_child(label)
            return listboxrow

    class Button(Gtk.Button):
        def create(
            text="",
            hexpand=False,
            vexpand=False,
            halign="fill",
            valign="start"
            ):
            button = Gtk.Button(label=text)
            button.set_hexpand(hexpand)
            button.set_vexpand(vexpand)
            button.set_halign(settings[halign])
            button.set_valign(settings[valign])
            return button

    class ListBoxRow(Gtk.ListBoxRow):
        def create(
            text="",
            hexpand=False,
            vexpand=False,
            halign='fill',
            valign="start",
            css=[]
            ):
            label = Gtk.Label(label=text)
            listboxrow = Gtk.ListBoxRow()
            listboxrow.set_child(label)
            listboxrow.set_css_classes(css)
            return listboxrow

