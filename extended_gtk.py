import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
      
      def __init__(self):
            Gtk.Winodw.__init__(self, title = "hello bangladesh")

            self.button = Gtk.Button(label = "click here, please")
            self.button.connect("clicked", self.on_button_clicked)
            self.add(self.button)

      def on_button_clicked(self, widget):
            print("Hello Bangladesh, I love you")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
