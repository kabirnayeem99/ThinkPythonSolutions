#thie is my first program on pygobject
#this one is about creating a
#basic_window

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

x = Gtk.Window()
x.connect("destroy", Gtk.main_quit)
x.show_all()
Gtk.main()
